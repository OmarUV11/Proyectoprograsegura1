#!/usr/bin/env bash

sleep 15

python3 -u manage.py makemigrations
python3 -u manage.py migrate

gunicorn --bind :8000 sistemaSeg.wsgi:application --reload

