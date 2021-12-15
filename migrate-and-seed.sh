#!/bin/bash

printf "Making migrations..."
python3 manage.py makemigrations

printf "\nMigrating..."
python3 manage.py migrate

python3 manage.py loaddata seed.json
