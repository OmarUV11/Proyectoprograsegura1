#!/usr/bin/env bash

sleep 15

python3 -u manage.py makemigrations
python3 -u manage.py migrate

su -c  'python3 -u /evaluacion/servidor.py 8002' usuario2

gunicorn --bind :8000 sistemaSeg.wsgi:application --reload

