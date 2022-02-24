# pjecz-citas-v2

Sistema de Citas version 2 front-end hecho con Flask

## Configurar

Crear entorno virtual python 3.8 o superior

    python -m venv venv
    . venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

Crear archivo `.env` con las variables de entorno

    # Flask
    FLASK_APP=citas_v2.app
    FLASK_DEBUG=1
    SECRET_KEY=****************

    # Database
    DB_HOST=127.0.0.1
    DB_NAME=pjecz_citas_v2
    DB_PASS=****************
    DB_USER=adminpjeczcitasv2

    # Google Cloud Storage
    CLOUD_STORAGE_DEPOSITO=

    # Salt para convertir/reconverir el id en hash
    SALT=****************

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
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pjecz_citas_v2.sqlite3'

En Fedora o Debian crear archivo `.bashrc` para facilitar la carga de las variables y el entorno virtual desde Konsole

    if [ -f ~/.bashrc ]; then
        source ~/.bashrc
    fi

    source venv/bin/activate
    if [ -f .env ]; then
        export $(grep -v '^#' .env | xargs)
    fi

    figlet Citas V2
    echo

    echo "-- Flask"
    echo "   FLASK_APP:   ${FLASK_APP}"
    echo "   FLASK_DEBUG: ${FLASK_DEBUG}"
    echo "   SECRET_KEY:  ${SECRET_KEY}"
    echo
    echo "-- Database"
    echo "   DB_HOST: ${DB_HOST}"
    echo "   DB_NAME: ${DB_NAME}"
    echo "   DB_PASS: ${DB_PASS}"
    echo "   DB_USER: ${DB_USER}"
    echo
    echo "-- Google Cloud Storage"
    echo "   CLOUD_STORAGE_DEPOSITO: ${CLOUD_STORAGE_DEPOSITO}"
    echo
    echo "-- Salt"
    echo "   SALT: ${SALT}"
    echo
    echo "-- Deployment environment"
    echo "   DEPLOYMENT_ENVIRONMENT: ${DEPLOYMENT_ENVIRONMENT}"
    echo

    export PGDATABASE=${DB_NAME}
    export PGPASSWORD=${DB_PASS}
    export PGUSER=${DB_USER}
    echo "-- PostgreSQL"
    echo "   PGDATABASE: ${PGDATABASE}"
    echo "   PGPASSWORD: ${PGPASSWORD}"
    echo "   PGUSER:     ${PGUSER}"
    echo
