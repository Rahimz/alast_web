from .base import *

SECRET_KEY = pro_secret_key

DEBUG = False

ALLOWED_HOSTS = ['alastdesign.com', 'www.alastdesign.com', server_ip]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASS,
        'HOST': 'localhost',
        'PORT': '',
    }
}

CSRF_TRUSTED_ORIGINS = [
    'https://alastdesign.com',
    'https://www.alastdesign.com',
]