"""
Flask App
"""
from flask import Flask
from redis import Redis
import rq
from citas_cliente.extensions import csrf, db, login_manager, moment

from citas_cliente.blueprints.sistemas.views import sistemas
from citas_cliente.blueprints.politicas.views import politicas
from citas_cliente.blueprints.cit_clientes.views import cit_cliente

from citas_cliente.blueprints.cit_clientes.models import CitCliente


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
    app.register_blueprint(sistemas)
    app.register_blueprint(cit_cliente)
    app.register_blueprint(politicas)
    # Cargar las extensiones
    extensions(app)
    authentication(CitCliente)
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
    login_manager.login_view = "cit_clientes.login"

    @login_manager.user_loader
    def load_user(uid):
        return user_model.query.get(uid)
