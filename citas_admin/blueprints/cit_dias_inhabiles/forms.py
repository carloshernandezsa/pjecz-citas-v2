"""
Cit Clientes, formularios
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, Optional


class CitDiaInhabilForm(FlaskForm):
    """Formulario CitDíasInhabiles"""

    fecha = DateField("Fecha", validators=[DataRequired()])
    descripcion = StringField("Descripción", validators=[Optional(), Length(max=512)])
    guardar = SubmitField("Guardar")
