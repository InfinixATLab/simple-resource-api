set -e

echo "Rodando Migrações..."
python manage.py migrate

echo "Coletando Arquivos Estáticos..."
python manage.py collectstatic --noinput

echo "Iniciando Servidor Gunicorn..."
gunicorn store_api.wsgi:application --bind 0.0.0.0:8000