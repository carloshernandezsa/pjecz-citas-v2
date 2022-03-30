"""
Usuarios, formularios
"""
from flask_wtf import FlaskForm
from wtforms import HiddenField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, Regexp

from lib.safe_string import CONTRASENA_REGEXP


CONTRASENA_MENSAJE = "De 8 a 48 caracteres con al menos una mayúscula, una minúscula y un número. No acentos, ni eñe."


class AccesoForm(FlaskForm):
    """Formulario de acceso al sistema"""

    siguiente = HiddenField()
    email = StringField("Correo electrónico", validators=[DataRequired(), Email()])
    contrasena = PasswordField("Contraseña", validators=[DataRequired(), Length(8, 48), Regexp(CONTRASENA_REGEXP, 0, CONTRASENA_MENSAJE)])
    guardar = SubmitField("Ingresar")


class CambiarContrasenaForm(FlaskForm):
    """Formulario para cambiar la contraseña"""

    contrasena_actual = PasswordField(
        "Contraseña actual",
        validators=[
            DataRequired(),
            Regexp(CONTRASENA_REGEXP, 0, CONTRASENA_MENSAJE),
        ],
    )
    contrasena = PasswordField(
        "Nueva contraseña",
        validators=[
            DataRequired(),
            Regexp(CONTRASENA_REGEXP, 0, CONTRASENA_MENSAJE),
            EqualTo("contrasena_repetir", message="Las contraseñas deben coincidir."),
        ],
    )
    contrasena_repetir = PasswordField("Repetir la nueva contraseña")
    actualizar = SubmitField("Actualizar")


class ClienteNewForm(FlaskForm):
    """Formulario para nuevo usuario"""

    nombres = StringField("Nombres", validators=[DataRequired(), Length(max=256)])
    apellido_paterno = StringField("Apellido paterno", validators=[DataRequired(), Length(max=256)])
    apellido_materno = StringField("Apellido materno", validators=[Optional(), Length(max=256)])
    telefono = StringField("Teléfono", validators=[Optional(), Length(max=32)])
    curp = StringField("CURP", validators=[DataRequired(), Length(max=18)])
    curp_repetir = StringField("Repetir CURP", validators=[DataRequired(), Length(max=18)])
    email = StringField("e-mail", validators=[DataRequired(), Email()])
    email_repetir = StringField("Repetir e-mail", validators=[DataRequired(), Email()])
    contrasena = PasswordField(
        "Contraseña",
        validators=[
            DataRequired(),
            Regexp(CONTRASENA_REGEXP, 0, CONTRASENA_MENSAJE),
            EqualTo("contrasena_repetir", message="Las contraseñas deben coincidir."),
        ],
    )
    contrasena_repetir = PasswordField("Repetir contraseña", validators=[DataRequired()])
    guardar = SubmitField("Registrar")


class UsuarioEditForm(FlaskForm):
    """Formulario para editar usuario"""

    nombres = StringField("Nombres", validators=[Optional(), Length(max=256)])
    apellido_paterno = StringField("Apellido paterno", validators=[Optional(), Length(max=256)])
    apellido_materno = StringField("Apellido materno", validators=[Optional(), Length(max=256)])
    curp = StringField("CURP", validators=[Optional(), Length(max=256)])
    puesto = StringField("Puesto", validators=[Optional(), Length(max=256)])
    email = StringField("e-mail")  # Read only
    guardar = SubmitField("Guardar")
