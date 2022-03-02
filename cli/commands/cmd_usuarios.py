"""
Usuarios

- nueva_contrasena: Cambiar contraseña de un usuario
- enviar_reporte: Enviar via correo electronico el reporte de usuarios
- sincronizar: Sincronizar usuarios con la API de RRHH Personal
"""
import click

from citas_v2.app import create_app
from citas_v2.extensions import db

from citas_v2.blueprints.usuarios.models import Usuario
from citas_v2.extensions import pwd_context

app = create_app()
db.app = app


@click.group()
def cli():
    """Usuarios"""


@click.command()
def definir_oficinas():
    """Definir las oficinas a partir de una relacion entre email y oficina"""
    app.task_queue.enqueue("citas_v2.blueprints.usuarios.tasks.definir_oficinas")
    click.echo("Definir oficinas se está ejecutando en el fondo.")


@click.command()
def enviar_reporte():
    """Enviar via correo electronico el reporte"""
    app.task_queue.enqueue("citas_v2.blueprints.usuarios.tasks.enviar_reporte")
    click.echo("Enviar reporte se está ejecutando en el fondo.")


@click.command()
def estandarizar():
    """Estandarizar nombres, apellidos y puestos en mayusculas"""
    app.task_queue.enqueue("citas_v2.blueprints.usuarios.tasks.estandarizar")
    click.echo("Estandarizar se está ejecutando en el fondo.")


@click.command()
@click.argument("email", type=str)
def nueva_contrasena(email):
    """Cambiar contraseña de un usuario"""
    usuario = Usuario.find_by_identity(email)
    if usuario is None:
        click.echo(f"No existe el e-mail {email} en usuarios")
        return
    contrasena_1 = input("Contraseña: ")
    contrasena_2 = input("De nuevo la misma contraseña: ")
    if contrasena_1 != contrasena_2:
        click.echo("No son iguales las contraseñas. Por favor intente de nuevo.")
        return
    usuario.contrasena = pwd_context.hash(contrasena_1.strip())
    usuario.save()
    click.echo(f"Se ha cambiado la contraseña de {email} en usuarios")


@click.command()
def sincronizar():
    """Sincronizar con RRHH Personal"""
    app.task_queue.enqueue("citas_v2.blueprints.usuarios.tasks.sincronizar")
    click.echo("Sincronizar se está ejecutando en el fondo.")


cli.add_command(definir_oficinas)
cli.add_command(enviar_reporte)
cli.add_command(estandarizar)
cli.add_command(nueva_contrasena)
cli.add_command(sincronizar)