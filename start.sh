#!/usr/bin/env bash

# Start Gunicorn processes
echo Starting Gunicorn.
#exec gunicorn SimilarPlaces.wsgi:application \
#    --bind 0.0.0.0:8000 \
#    --workers 3
exec python manage.py runserver 0.0.0.0:$PORT