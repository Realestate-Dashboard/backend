#!/bin/sh

set -e 

echo "${0}: running migrations. :"
python manage.py makemigrations accounts
python manage.py makemigrations dashboard
python manage.py migrate --noinput

echo "${0} : collect staticfile "
python manage.py collectstatic --noinput

gunicorn config.wsgi --bind 0.0.0.0:8000
  
