#!/usr/bin/env bash
echo "Applying database migrations"
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

echo "Starting Gunicorn"
exec gunicorn config.wsgi --user www-data --bind 0.0.0.0:8000 --workers 3 --timeout 10 --workers 3 --log-file=- --log-level debug