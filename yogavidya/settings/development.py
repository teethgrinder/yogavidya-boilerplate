# -*- coding: utf-8 -*-
from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '7ig$oax5u^kscl2&luld&htts@4a=sq29zu6($+oix@v7=k7)q'
 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DATABASE_NAME'),
        'USER': get_env_variable('DATABASE_USER'),
        'PASSWORD': get_env_variable('DATABASE_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
 
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)