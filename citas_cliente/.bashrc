if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi

source venv/bin/activate
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi
export FLASK_APP=citas_cliente.app
export SECRET_KEY=DrZWCj6hxlM2A35M
export HOST=http://127.0.0.1:5011

figlet CitasV2 cliente
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
echo "-- Redis"
echo "   REDIS_URL:  ${REDIS_URL}"
echo "   TASK_QUEUE: ${TASK_QUEUE}"
echo
echo "-- Google Cloud Storage"
echo "   CLOUD_STORAGE_DEPOSITO: ${CLOUD_STORAGE_DEPOSITO}"
echo
echo "-- Host"
echo "   HOST: ${HOST}"
echo
echo "-- Salt"
echo "   SALT: ${SALT}"
echo
echo "-- Deployment environment"
echo "   DEPLOYMENT_ENVIRONMENT: ${DEPLOYMENT_ENVIRONMENT}"
echo

alias arrancar="flask run --port 5011"
echo "-- Aliases"
echo "   arrancar: flask run --port 5011"
echo
