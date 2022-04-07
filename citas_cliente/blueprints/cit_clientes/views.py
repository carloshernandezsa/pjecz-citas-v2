"""
CitClientes, vistas
"""
import os
import re
from datetime import datetime
from dateutil.relativedelta import relativedelta
from lib.pwgen import generar_contrasena
from pytz import timezone
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from lib.safe_next_url import safe_next_url
from lib.safe_string import CONTRASENA_REGEXP, EMAIL_REGEXP, TOKEN_REGEXP, safe_string, safe_message

from citas_admin.extensions import pwd_context
from citas_admin.blueprints.usuarios.decorators import anonymous_required

from citas_cliente.blueprints.cit_clientes.models import CitCliente
from citas_cliente.blueprints.cit_clientes.forms import AccesoForm, ClienteNewForm

MODULO = "CIT CLIENTES"

cit_cliente = Blueprint("cit_clientes", __name__, template_folder="templates")


@cit_cliente.route("/login", methods=["GET", "POST"])
@anonymous_required()
def login():
    """Acceso al Sistema"""
    form = AccesoForm(siguiente=request.args.get("siguiente"))
    if form.validate_on_submit():
        # Tomar valores del formulario
        identidad = request.form.get("email")
        contrasena = request.form.get("contrasena")
        siguiente_url = request.form.get("siguiente")

        # De lo contrario, el ingreso es con username/password
        if re.fullmatch(EMAIL_REGEXP, identidad) is None:
            flash("Correo electrónico no válido.", "warning")
        elif re.fullmatch(CONTRASENA_REGEXP, contrasena) is None:
            flash("Contraseña no válida.", "warning")
        else:
            cliente = CitCliente.find_by_identity(identidad)
            if cliente and cliente.authenticated(password=contrasena):
                if login_user(cliente, remember=True) and cliente.is_active:
                    if siguiente_url:
                        return redirect(safe_next_url(siguiente_url))
                    return redirect(url_for("sistemas.start"))
                else:
                    flash("No está activa esa cuenta", "warning")
            else:
                flash("Usuario o contraseña incorrectos.", "warning")
    return render_template("cit_clientes/login.jinja2", form=form, title="Citas v2")


@cit_cliente.route("/logout")
@login_required
def logout():
    """Salir del Sistema"""
    logout_user()
    flash("Ha salido de este sistema.", "success")
    return redirect(url_for("cit_clientes.login"))


@cit_cliente.route("/perfil")
@login_required
def profile():
    """Mostrar el Perfil"""
    ahora_utc = datetime.now(timezone("UTC"))
    ahora_mx_coah = ahora_utc.astimezone(timezone("America/Mexico_City"))
    formato_fecha = "%Y-%m-%d"
    return render_template(
        "login/profile.jinja2",  
        ahora_utc_str=ahora_utc.strftime(formato_fecha),
        ahora_mx_coah_str=ahora_mx_coah.strftime(formato_fecha),
    )
       


@cit_cliente.route("/nuevo_registro", methods=["GET", "POST"])
def new():
    """Nuevo registro para clientes"""
    form = ClienteNewForm()
    validacion = False
    if form.validate_on_submit():
        try:
            validacion = _validar_new_cliente(form)
        except Exception as err:
            flash(f"Creación del nuevo Cliente incorrecto. {str(err)}", "warning")
            validacion = False

        if validacion:
            cliente = CitCliente(
                nombres=safe_string(form.nombres.data),
                apellido_paterno=safe_string(form.apellido_paterno.data),
                apellido_materno=safe_string(form.apellido_materno.data),
                curp=safe_string(form.curp.data),
                telefono=safe_string(form.telefono.data),
                email=form.email.data,
                contrasena=pwd_context.hash(form.contrasena.data),
                hash=pwd_context.hash(generar_contrasena()),
                renovacion_fecha=date.today() + relativedelta(months=12),
            )
            cliente.save()
            return redirect(url_for("cit_clientes.login"))
    return render_template("cit_clientes/new.jinja2", form=form)


def _validar_new_cliente(form: ClienteNewForm):
    """Validación para la creación de un nuevo registro de cliente"""
    if form.contrasena.data != form.contrasena_repetir.data:
        raise Exception("Las contraseñas no coinciden.")
    if form.curp.data != form.curp_repetir.data:
        raise Exception("Las claves CURP no coinciden.")
    if form.email.data != form.email_repetir.data:
        raise Exception("Los e-mails no coinciden.")

    return True
