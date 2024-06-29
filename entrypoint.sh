#!/bin/sh


until nc -z postgres 5432; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "Postgres is up - executing commands"


python manage.py makemigrations
python manage.py migrate


daphne -b 0.0.0.0 -p 80 sm2.asgi:application
