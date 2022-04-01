"""
Modulos, vistas
"""
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from lib.safe_string import safe_message, safe_string
from citas_admin.blueprints.usuarios.decorators import permission_required

from citas_admin.blueprints.bitacoras.models import Bitacora
from citas_admin.blueprints.modulos.models import Modulo
from citas_admin.blueprints.modulos.forms import ModuloForm
from citas_admin.blueprints.permisos.models import Permiso

MODULO = "MODULOS"

modulos = Blueprint("modulos", __name__, template_folder="templates")


@modulos.before_request
@login_required
@permission_required(MODULO, Permiso.VER)
def before_request():
    """Permiso por defecto"""


@modulos.route("/modulos")
def list_active():
    """Listado de Modulos activos"""
    return render_template(
        "modulos/list.jinja2",
        modulos=Modulo.query.filter_by(estatus="A").all(),
        titulo="Módulos",
        estatus="A",
    )


@modulos.route("/modulos/inactivos")
@permission_required(MODULO, Permiso.MODIFICAR)
def list_inactive():
    """Listado de Modulos inactivos"""
    return render_template(
        "modulos/list.jinja2",
        modulos=Modulo.query.filter_by(estatus="B").all(),
        titulo="Módulos inactivos",
        estatus="B",
    )


@modulos.route("/modulos/<int:modulo_id>")
def detail(modulo_id):
    """Detalle de un Modulo"""
    modulo = Modulo.query.get_or_404(modulo_id)
    return render_template("modulos/detail.jinja2", modulo=modulo)


@modulos.route("/modulos/nuevo", methods=["GET", "POST"])
@permission_required(MODULO, Permiso.CREAR)
def new():
    """Nuevo Modulo"""
    form = ModuloForm()
    if form.validate_on_submit():
        # Validar que el nombre no se repita
        nombre = safe_string(form.nombre.data)
        if Modulo.query.filter_by(nombre=nombre).first():
            flash("La nombre ya está en uso. Debe de ser único.", "warning")
        else:
            modulo = Modulo(
                nombre=nombre,
                nombre_corto=form.nombre_corto.data,
                icono=form.icono.data,
                ruta=form.ruta.data,
                en_navegacion=form.en_navegacion.data == 1,
            )
            modulo.save()
            bitacora = Bitacora(
                modulo=Modulo.query.filter_by(nombre=MODULO).first(),
                usuario=current_user,
                descripcion=safe_message(f"Nuevo módulo {modulo.nombre}"),
                url=url_for("modulos.detail", modulo_id=modulo.id),
            )
            bitacora.save()
            flash(bitacora.descripcion, "success")
            return redirect(bitacora.url)
    return render_template("modulos/new.jinja2", form=form)


@modulos.route("/modulos/edicion/<int:modulo_id>", methods=["GET", "POST"])
@permission_required(MODULO, Permiso.MODIFICAR)
def edit(modulo_id):
    """Editar Modulo"""
    modulo = Modulo.query.get_or_404(modulo_id)
    form = ModuloForm()
    if form.validate_on_submit():
        es_valido = True
        # Si cambia el nombre verificar que no este en uso
        nombre = safe_string(form.nombre.data)
        if modulo.nombre != nombre:
            modulo_existente = Modulo.query.filter_by(nombre=nombre).first()
            if modulo_existente and modulo_existente.id != modulo.id:
                es_valido = False
                flash("El nombre ya está en uso. Debe de ser único.", "warning")
        # Si es valido actualizar
        if es_valido:
            modulo.nombre = nombre
            modulo.nombre_corto = safe_string(form.nombre_corto.data)
            modulo.icono = form.icono.data
            modulo.ruta = form.ruta.data
            modulo.en_navegacion = form.en_navegacion.data == 1
            modulo.save()
            bitacora = Bitacora(
                modulo=Modulo.query.filter_by(nombre=MODULO).first(),
                usuario=current_user,
                descripcion=safe_message(f"Editado módulo {modulo.nombre}"),
                url=url_for("modulos.detail", modulo_id=modulo.id),
            )
            bitacora.save()
            flash(bitacora.descripcion, "success")
            return redirect(bitacora.url)
    form.nombre.data = modulo.nombre
    form.nombre_corto.data = modulo.nombre_corto
    form.icono.data = modulo.icono
    form.ruta.data = modulo.ruta
    if modulo.en_navegacion:
        form.en_navegacion.data = 1
    else:
        form.en_navegacion.data = 0
    return render_template("modulos/edit.jinja2", form=form, modulo=modulo)


@modulos.route("/modulos/eliminar/<int:modulo_id>")
@permission_required(MODULO, Permiso.MODIFICAR)
def delete(modulo_id):
    """Eliminar Modulo"""
    modulo = Modulo.query.get_or_404(modulo_id)
    if modulo.estatus == "A":
        modulo.delete()
        bitacora = Bitacora(
            modulo=Modulo.query.filter_by(nombre=MODULO).first(),
            usuario=current_user,
            descripcion=safe_message(f"Eliminado módulo {modulo.nombre}"),
            url=url_for("modulos.detail", modulo_id=modulo.id),
        )
        bitacora.save()
        flash(bitacora.descripcion, "success")
        return redirect(bitacora.url)
    return redirect(url_for("modulos.detail", modulo_id=modulo.id))


@modulos.route("/modulos/recuperar/<int:modulo_id>")
@permission_required(MODULO, Permiso.MODIFICAR)
def recover(modulo_id):
    """Recuperar Modulo"""
    modulo = Modulo.query.get_or_404(modulo_id)
    if modulo.estatus == "B":
        modulo.recover()
        bitacora = Bitacora(
            modulo=Modulo.query.filter_by(nombre=MODULO).first(),
            usuario=current_user,
            descripcion=safe_message(f"Recuperado módulo {modulo.nombre}"),
            url=url_for("modulos.detail", modulo_id=modulo.id),
        )
        bitacora.save()
        flash(bitacora.descripcion, "success")
        return redirect(bitacora.url)
    return redirect(url_for("modulos.detail", modulo_id=modulo.id))