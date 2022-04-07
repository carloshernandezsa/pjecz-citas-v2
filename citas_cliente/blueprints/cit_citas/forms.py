"""
Cit Citas, formularios
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class CitCitaForm(FlaskForm):
    """Formulario CitCita"""

    nombre = StringField("Nombre", validators=[DataRequired(), Length(max=256)])
    descripcion = StringField("Descripción", validators=[DataRequired(), Length(max=256)])
    guardar = SubmitField("Guardar")
