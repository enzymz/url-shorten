from .base import *
import os

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'POST': os.environ.get('DATABASE_POST'),
    }
}

DEBUG = True

ADMIN = [('Ha',os.environ.get('ADMIN_MAIL'))]

ALLOWED_HOSTS = ['url-shorten-6102.herokuapp.com']

PROJECT_ROOT = os.path.dirname(os.path.abspath('xurl'))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

SITE_ID = 2
