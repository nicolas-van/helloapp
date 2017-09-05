
from helloapp.settings import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': './db.sqlite3',
    }
}

"""
'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': 'mydb',                      # Or path to database file if using sqlite3.
    # The following settings are not used with sqlite3:
    'USER': 'myuser',
    'PASSWORD': 'password',
    'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
    'PORT': '',                      # Set to empty string for default.
}
"""
