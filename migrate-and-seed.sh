#!/bin/bash
echo "Making migrations..."
python3 manage.py makemigrations

printf "\nMigrating..."
python3 manage.py migrate

printf "\nSeeding "
python3 manage.py loaddata seed.json
