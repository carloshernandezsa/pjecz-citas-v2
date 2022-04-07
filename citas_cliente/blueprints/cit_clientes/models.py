"""
Cit Clientes, modelos
"""
from flask_login import UserMixin

from lib.universal_mixin import UniversalMixin
from citas_admin.extensions import db, pwd_context


class CitCliente(db.Model, UserMixin, UniversalMixin):
    """Cit Cliente"""

    # Nombre de la tabla
    __tablename__ = "cit_clientes"

    # Clave primaria
    id = db.Column(db.Integer, primary_key=True)

    # Columnas
    nombres = db.Column(db.String(256), nullable=False)
    apellido_paterno = db.Column(db.String(256), nullable=False)
    apellido_materno = db.Column(db.String(256), default="", server_default="")
    curp = db.Column(db.String(18), unique=True, nullable=False)
    telefono = db.Column(db.String(64), default="", server_default="")
    email = db.Column(db.String(256), unique=True, nullable=False)
    contrasena = db.Column(db.String(256), nullable=False)
    hash = db.Column(db.String(256), default="", server_default="")
    renovacion_fecha = db.Column(db.Date(), nullable=False)

    # Hijos
    cit_citas = db.relationship("CitCita", back_populates="cit_cliente")

    @property
    def nombre(self):
        """Junta nombres, apellido_paterno y apellido materno"""
        return self.nombres + " " + self.apellido_paterno + " " + self.apellido_materno

    @classmethod
    def find_by_identity(cls, identity):
        """Encontrar a un cliente por su correo electrónico"""
        return CitCliente.query.filter(CitCliente.email == identity).first()

    @property
    def is_active(self):
        """¿Es activo?"""
        return self.estatus == "A"

    def authenticated(self, with_password=True, password=""):
        """Ensure a user is authenticated, and optionally check their password."""
        if self.id and with_password:
            return pwd_context.verify(password, self.contrasena)
        return True

    def __repr__(self):
        """Representación"""
        return f"<CitCliente {self.email}>"
