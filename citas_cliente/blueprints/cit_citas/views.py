"""
citasr cita, vistas
"""
import json
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from lib.datatables import get_datatable_parameters, output_datatable_json
from lib.safe_string import safe_string, safe_message


from citas_cliente.blueprints.cit_citas.models import CitCita
from citas_cliente.blueprints.cit_citas.forms import CitCitaForm

MODULO = "CIT CITAS"

cit_citas = Blueprint("cit_citas", __name__, template_folder="templates")


@cit_citas.before_request
@login_required
def before_request():
    """Permiso por defecto"""


@cit_citas.route("/cit_citas")
def list_active():
    """Listado de Citas activos"""
    return render_template(
        "cit_citas/list_active.jinja2",
        filtros=json.dumps({"estatus": "A"}),
        titulo="Citas",
        estatus="A",
    )


@cit_citas.route("/cit_citas/inactivos")
def list_inactive():
    """Listado de citas inactivos"""
    return render_template(
        "cit_citas/list.jinja2",
        filtros=json.dumps({"estatus": "B"}),
        titulo="citas inactivos",
        estatus="B",
    )


@cit_citas.route("/cit_citas/<int:cit_cita_id>")
def detail(cit_cita_id):
    """Detalle de un Citas"""
    cit_cita = CitCita.query.get_or_404(cit_cita_id)
    return render_template("cit_citas/detail.jinja2", cit_cita=cit_cita)


@cit_citas.route("/cit_citas/nuevo", methods=["GET", "POST"])
def new():
    """Nuevo citas"""
    form = CitCitaForm()
    if form.validate_on_submit():
        cit_cita = CitCita(
            distritos=safe_string(form.distritos.data),
            juzgados=safe_string(form.juzgados.data),
            tipo_tramite=safe_string(form.tipo_tramite.data),
            indicaciones_tramite=safe_string(form.indicaciones_tramite.data),
            # fecha=form.fecha.data,
            # hora=form.hora.data,
        )
        cit_cita.save()
        flash("Datos incorrectos.", "warning")
        redirect(url_for("cit_citas.detail", cit_cita=cit_cita.id))
    return render_template("cit_citas/new.jinja2", form=form)
