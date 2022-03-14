"""
CITAS Servicios, modelos
"""
from enum import unique
from citas_backend.extensions import db
from lib.universal_mixin import UniversalMixin


class CitServicio(db.Model, UniversalMixin):
    """CITServicio"""

    # Nombre de la tabla
    __tablename__ = "cit_servicios"

    # Clave primaria
    id = db.Column(db.Integer, primary_key=True)

    # Clave foránea

    # Columnas
    clave = db.Column(db.String(32), unique=True, nullable=False)
    nombre = db.Column(db.String(128), nullable=False)
    solicitar_expedientes = db.Column(db.Boolean, nullable=False)
    duracion = db.Column(db.Time(), nullable=False)

    # Hijos

    def __repr__(self):
        """Representación"""
        return "<CIT_Servicios>"
