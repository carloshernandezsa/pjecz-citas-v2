"""
Políticas

    - Aviso de privacidad
    - Términos y Condiciones
"""
from flask import Blueprint, redirect, render_template
import markdown

politicas = Blueprint("politicas", __name__, template_folder="templates")


@politicas.route("/politicas/aviso_privacidad")
def aviso_privacidad():
    """Aviso de Privacidad"""
    titulo = "Aviso de Privacidad"
    with open("citas_cliente/static/md/aviso_privacidad.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)
    return render_template("politicas/display.jinja2", titulo=titulo, texto=html)


@politicas.route("/politicas/terminos_condiciones")
def terminos_condiciones():
    """Términos y Condiciones"""
    titulo = "Términos y Condiciones"
    with open("citas_cliente/static/md/terminos_condiciones.md", "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)
    return render_template("politicas/display.jinja2", titulo=titulo, texto=html)
