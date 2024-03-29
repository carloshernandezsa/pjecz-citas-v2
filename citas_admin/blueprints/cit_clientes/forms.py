"""
Cit Clientes, formularios
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, Optional, Email


class CitClienteSearchForm(FlaskForm):
    """Formulario para buscar Clientes"""

    nombres = StringField("Nombres", validators=[Optional(), Length(max=256)])
    apellido_paterno = StringField("Apellido Paterno", validators=[Optional(), Length(max=256)])
    apellido_materno = StringField("Apellido Materno", validators=[Optional(), Length(max=256)])
    curp = StringField("CURP", validators=[Optional(), Length(max=18)])
    telefono = StringField("Teléfono", validators=[Optional(), Length(max=64)])
    email = StringField("Correo electrónico", validators=[Optional(), Email()])
    buscar = SubmitField("Buscar")
