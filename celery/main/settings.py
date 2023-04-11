"""
Django settings for main project.
Generated by 'django-admin startproject' using Django 3.2.11.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from importlib import import_module
from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = Path(__file__).resolve().parent.parent

# local settings
if not os.environ.get('CIRCLE_CI_WORKFLOW'):
    local_settings = import_module('main.local_settings')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

if not os.environ.get('CIRCLE_CI_WORKFLOW'):
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = local_settings.SECRET_KEY
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = local_settings.DEBUG
    LOCAL_DATABASES = local_settings.LOCAL_DATABASES
else:
    SECRET_KEY = 'secret_circle_ci_key'
    DEBUG = True
    LOCAL_DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django_ci',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': 5432,
        }
    }

ALLOWED_HOSTS = ['pingeandoando.tk', 'app', 'web', 'localhost']

# CELERY CONFIG
# https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html
CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
# https://docs.celeryq.dev/en/3.1/configuration.html
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# Configure Celery to use a custom time zone.
CELERY_TIMEZONE = "America/Santiago"
# A sequence of modules to import when the worker starts
CELERY_IMPORTS = ('base.tasks',)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # internals
    'base.apps.BaseConfig',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [''],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {}
DATABASES.update(LOCAL_DATABASES)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# static
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static/')
STATIC_URL = '/static/'
# media
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media/')
MEDIA_URL = '/uploads/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'