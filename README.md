# pjecz-citas-v2

Sistema de Citas version 2 front-end hecho con Flask

## Configurar

Crear entorno virtual python 3.8 o superior

    python -m venv venv
    . venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

Crear archivo `.env` con las variables de entorno generales.

Observe que en el repositorio archivos para arrancar Konsole en `citas_admin/.bashrc` y  `citas_cliente/.bashrc`

**Deje vacias** a `FLASK_APP`, `SECRET_KEY` y `HOST` porque `.bashrc` las define.

    # Flask
    FLASK_APP=
    FLASK_DEBUG=1
    SECRET_KEY=

    # Database
    DB_HOST=127.0.0.1
    DB_NAME=pjecz_citas_v2
    DB_PASS=****************
    DB_USER=adminpjeczcitasv2

    # Redis
    REDIS_URL=redis://127.0.0.1
    TASK_QUEUE=pjecz_citas_v2

    # Google Cloud Storage
    CLOUD_STORAGE_DEPOSITO=

    # Host
    HOST=

    # Salt para convertir/reconverir el id en hash
    SALT=

    # Sendgrid
    SENDGRID_API_KEY=
    SENDGRID_FROM_EMAIL=
    SENDGRID_TO_EMAIL_REPORTES=

    # Si esta en PRODUCTION se evita reiniciar la base de datos
    DEPLOYMENT_ENVIRONMENT=develop

Crear archivo `instance/settings.py` con la configuracion para desarrollo

    import os

    # Base de datos
    DB_USER = os.environ.get("DB_USER", "wronguser")
    DB_PASS = os.environ.get("DB_PASS", "badpassword")
    DB_NAME = os.environ.get("DB_NAME", "pjecz_citas_v2")
    DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")

    # MySQL
    # SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

    # PostgreSQL
    # SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

    # SQLite
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///pjecz_citas_v2.sqlite3'

**Quite el comentario en la base de datos que use.**

En Konsole haga un perfil de nombre **GitHub pjecz-citas-v2 admin**

    /bin/bash --rcfile citas_admin/.bashrc

Y otro perfil de nombre  **GitHub pjecz-citas-v2 cliente**

    /bin/bash --rcfile citas_cliente/.bashrc

Abra una terminal para cada perfil
