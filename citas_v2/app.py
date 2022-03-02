"""
Flask App
"""
from flask import Flask
from redis import Redis
import rq
from citas_v2.extensions import csrf, db, login_manager, moment

from citas_v2.blueprints.autoridades.views import autoridades
from citas_v2.blueprints.distritos.views import distritos
from citas_v2.blueprints.domicilios.views import domicilios
from citas_v2.blueprints.entradas_salidas.views import entradas_salidas
from citas_v2.blueprints.materias.views import materias
from citas_v2.blueprints.modulos.views import modulos
from citas_v2.blueprints.oficinas.views import oficinas
from citas_v2.blueprints.permisos.views import permisos
from citas_v2.blueprints.roles.views import roles
from citas_v2.blueprints.sistemas.views import sistemas
from citas_v2.blueprints.tareas.views import tareas
from citas_v2.blueprints.usuarios.views import usuarios
from citas_v2.blueprints.usuarios_roles.views import usuarios_roles


def create_app():
    """Crear app"""
    # Definir app
    app = Flask(__name__, instance_relative_config=True)
    # Cargar la configuración para producción en config/settings.py
    app.config.from_object("config.settings")
    # Cargar la configuración para desarrollo en instance/settings.py
    app.config.from_pyfile("settings.py", silent=True)
    # Redis
    app.redis = Redis.from_url(app.config["REDIS_URL"])
    app.task_queue = rq.Queue(app.config["TASK_QUEUE"], connection=app.redis, default_timeout=1920)
    # Cargar los blueprints
    app.register_blueprint(autoridades)
    app.register_blueprint(distritos)
    app.register_blueprint(domicilios)
    app.register_blueprint(entradas_salidas)
    app.register_blueprint(materias)
    app.register_blueprint(modulos)
    app.register_blueprint(oficinas)
    app.register_blueprint(permisos)
    app.register_blueprint(roles)
    app.register_blueprint(sistemas)
    app.register_blueprint(tareas)
    app.register_blueprint(usuarios)
    app.register_blueprint(usuarios_roles)
    # Cargar las extensiones
    extensions(app)
    # authentication(Usuario)
    # Entregar app
    return app


def extensions(app):
    """Incorporar las extensiones"""
    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)


def authentication(user_model):
    """Inicializar Flask-Login"""
    login_manager.login_view = "usuarios.login"

    @login_manager.user_loader
    def load_user(uid):
        return user_model.query.get(uid)
