#!/bin/sh
export DJANGO_SETTINGS_MODULE=prod_settings
./manage.py "$@"
