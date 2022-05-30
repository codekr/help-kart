#!/bin/bash

set -e

./manage.py migrate
./manage.py collectstatic --noinput
./manage.py createsuperuser --noinput

exec tail -f /dev/null
