#!/bin/bash

set -o errexit
set -o nounset

printf "Making migrations..."
python3 manage.py makemigrations

printf "\nMigrating..."
python3 manage.py migrate --no-input

printf "\nLoading fixtures..."
python3 manage.py loaddata seed.json

printf "\mStarting server..."
python3 manage.py runserver 0.0.0.0:8000

exec "$@"
