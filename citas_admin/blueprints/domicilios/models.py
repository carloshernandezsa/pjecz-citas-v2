"""
Domicilios, modelos
"""
from citas_admin.extensions import db
from lib.universal_mixin import UniversalMixin


class Domicilio(db.Model, UniversalMixin):
    """Domicilio"""

    # Nombre de la tabla
    __tablename__ = "domicilios"

    # Clave primaria
    id = db.Column(db.Integer, primary_key=True)

    # Columnas
    estado = db.Column(db.String(64), nullable=False)
    municipio = db.Column(db.String(64), nullable=False)
    calle = db.Column(db.String(256), nullable=False)
    num_ext = db.Column(db.String(24), nullable=False, default="", server_default="")
    num_int = db.Column(db.String(24), nullable=False, default="", server_default="")
    colonia = db.Column(db.String(256), nullable=False, default="", server_default="")
    cp = db.Column(db.Integer(), nullable=False)
    completo = db.Column(db.String(1024), nullable=False, default="", server_default="")

    # Hijos
    oficinas = db.relationship("Oficina", back_populates="domicilio")
    cit_clientes = db.relationship("CitCliente", back_populates="domicilio")

    def __repr__(self):
        """Representación"""
        return f"<Domicilio {self.completo}>"