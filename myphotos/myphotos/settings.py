"""
Django settings for myphotos project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
#encoding:utf-8
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROUTE = os.path.dirname(os.path.realpath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&_n8)eizsg!na3u=^tpe%4z1qaxiuh3&&&c!-=i-n4o+zzyrk1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ADMINS = (('Luis Miguel Cuende', 'lmcuende@gmail.com'),)

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (os.path.join(PROJECT_ROUTE,'templates'),)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'mainapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myphotos.urls'

MEDIA_ROOT = os.path.join(PROJECT_ROUTE,'uploads')

MEDIA_URL = 'http://127.0.0.1:8000/media/'

WSGI_APPLICATION = 'myphotos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myphotosdb',
        'USER': 'luismiguel',
        'PASSWORD': 'desarrollo',
        'HOST': '',
        'PORT': '', 
    }
}
SITE_ID = 1
# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = (os.path.join(PROJECT_ROUTE,'static'),)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_ROOT = ''

STATIC_URL = '/static/'

#To send emails using gmail
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'proyectoasturix@gmail.com'
EMAIL_HOST_PASSWORD = 'AsturixProject2014'
EMAIL_PORT = 587