"""
Cit Citas, formularios
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TimeField
from wtforms.validators import DataRequired, Length, Optional


class CitCitaForm(FlaskForm):
    """Formulario CitCita"""

    distritos = StringField("Distrito Judicial", validators=[DataRequired(), Length(max=256)])
    juzgados = StringField("Juzgado o Unidad Administrativa", validators=[DataRequired(), Length(max=256)])
    tipo_tramite = StringField("Tipo de tramite", validators=[DataRequired()])
    indicaciones_tramite = StringField("Indicaciones del tramite", validators=[Optional()])
    # fecha = DateField("Fecha", format="%Y-%m-%d", validators=[DataRequired()])
    # hora = TimeField("Hora:Minuto", format="%H:%M", validators=[DataRequired()])
    guardar = SubmitField("Guardar")
