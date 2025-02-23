"""YANG Suite production deployment settings."""

import os

from yangsuite.settings.base import *     # noqa

# SECURITY WARNING: keep the secret key used in production secret!

if 'YANGSUITE_DB_PASSWORD' in os.environ:
    SECRET_KEY = os.environ['YANGSUITE_DB_PASSWORD']
else:
    raise(Exception('YANGSUITE_DB_PASSWORD not set'))

DEBUG = False

if 'DJANGO_ALLOWED_HOSTS' in os.environ:
    ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost').split()
    CSRF_TRUSTED_ORIGINS = []
    for ALLOWED_HOST in ALLOWED_HOSTS:
        CSRF_TRUSTED_ORIGINS.append(f'https://{ALLOWED_HOST}')

else:
    ALLOWED_HOSTS = 'localhost'

# Location to where static files will be collected
STATIC_ROOT = os.getenv('DJANGO_STATIC_ROOT', './ys-static')

# HTTPS settings
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

DATABASE_DEFAULT = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(MEDIA_ROOT, 'db.sqlite3'),
    'OPTIONS': {
        'timeout': 180
    }
}

DATABASE_POSTGRESQL = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'yangsuite',
    'USER': 'yangsuite',
    'PASSWORD': os.getenv('YANGSUITE_DB_PASSWORD'),
    'HOST': os.getenv('YANGSUITE_DB_HOST'),
    'PORT': os.getenv('YANGSUITE_DB_RW_SERVICE_PORT'),
}

DATABASES = {
    'default': DATABASE_POSTGRESQL
}
