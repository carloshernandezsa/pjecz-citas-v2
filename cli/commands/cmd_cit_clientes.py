"""
Cit Clientes

- nueva_cliente: Crear un nuevo cliente
- nueva_contrasena: Cambiar contraseña de un cliente
"""
import click

from citas_admin.app import create_app
from citas_admin.extensions import db

app = create_app()
db.app = app


@click.group()
def cli():
    """Cit Clientes"""


@click.command()
@click.argument("email", type=str)
def nuevo_cliente(email):
    """Crear un nuevo cliente"""


@click.command()
@click.argument("email", type=str)
def nueva_contrasena(email):
    """Cambiar contraseña de un cliente"""


cli.add_command(nuevo_cliente)
cli.add_command(nueva_contrasena)
