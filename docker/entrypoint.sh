#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

echo "[1/4] >>> Running migrations..."
python manage.py migrate
echo "[1/4] <<< Migration done"

echo "[2/4] >>> Importing datas into database..."
. /usr/src/.env
# export PGPASSWORD=$POSTGRES_PASSWORD
# psql --host=$POSTGRES_HOST --username=$POSTGRES_USER --dbname=$POSTGRES_DB -a -f ./init.sql
echo "[2/4] <<< Importation done"

echo "[3/4] >>> Creating super user..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$DJANGO_ADMIN', '$DJANGO_ADMIN_PASSWORD')" | python3 manage.py shell &>/dev/null
echo "[3/4] <<< Super User created"

echo "[4/4] >>> Starting server in development..."
python manage.py runserver 0.0.0.0:8000
echo "[4/4] <<< Server started"