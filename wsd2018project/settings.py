"""
Django settings for wsd2018project project on Heroku. For more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys
import platform
import dj_database_url
import django_heroku
import cloudinary

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# this is same for everyone – you should probably alter it!
SECRET_KEY = "l1o5frp%a^li6j^o1dpc11uzs$jp74)aebk#wmvr2bk^he(my6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (sys.argv[1] == 'runserver')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'ajax_select',
    'bootstrapform',
    'cloudinary',
    'simple_email_confirmation',
    'social_django',
    'font_awesome',
    'gamestore',
    'api',
    'django_social_share',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = 'wsd2018project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'wsd2018project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if platform.system() == "Windows":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        }
    }
else:
    DATABASES = {
        'default': {
            # the default database that "ships with" Django is sqlite
            # that is, however, not something you would be using with a
            # real production site. for that reason we're goingo to use
            # the industry standard PostgreSQL

            # 'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'wsd2018project'
            # if you want to define user, password etc.
            # do it here
        }
    }

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Helsinki'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config(conn_max_age=500, ssl_require=True))

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Rerdirect all traffic to HTTPS on server
SECURE_SSL_REDIRECT = (sys.argv[1] != 'runserver')

# Allow all host headers
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'django-reinhardt.herokuapp.com']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

MEDIAFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'media'),
]

# Cloudinary configs (For media uploads)
cloudinary.config(
  cloud_name="hvghogo4k",
  api_key="669877485749132",
  api_secret="H8TP_T7ormYatxRHk94ZfnIQKyM"
)

LOGIN_REDIRECT_URL = "/"
AUTH_USER_MODEL = 'gamestore.User'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'django.reinhardt.gamestore@gmail.com'
EMAIL_HOST_PASSWORD = 'DjangoReinhardt123'
EMAIL_PORT = 587

SOCIAL_AUTH_FACEBOOK_KEY = '428106740936543'
SOCIAL_AUTH_FACEBOOK_SECRET = 'a809665c92509ce9bf4ab9267066f0de'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SITE_ID = 1

# django-ajax-selects settings
AJAX_SELECT_BOOTSTRAP = False

# Activate Django-Heroku.
django_heroku.settings(locals())
