"""
Django settings for web_site project.

Generated by 'django-admin startproject' using Django 3.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

APP_NAME = os.environ.get('APP_NAME', os.path.basename(BASE_DIR))
SITE_DIR = os.environ.get(
    'SITE_DIR',
    os.path.abspath(os.path.join(BASE_DIR, '../../data', APP_NAME))
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r_6hz41%v#2u2wzxr7z5%$ypxvn4f+26bth3267ewhqc3mie&f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'app04_movies',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

WSGI_APPLICATION = 'web_site.wsgi.application'
ROOT_URLCONF = 'web_site.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # [os.path.join(BASE_DIR, 'templates'],
        # 'APP_DIRS': True,
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


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':       'django.db.backends.postgresql_psycopg2',
        'NAME':         os.environ.get('DB_NAME',       'postgres'),
        'USER':         os.environ.get('DB_USER',       'postgres'),
        'PASSWORD':     os.environ.get('DB_PASSWORD',   'postgres'),
        'HOST':         os.environ.get('DB_HOST',       'localhost'),
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CKEDITOR_UPLOAD_PATH = "uploads/"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
APPEND_SLASH = True
# ------------------------------------------------------------------------------


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(SITE_DIR, 'static'))
MEDIA_ROOT = os.path.join(SITE_DIR, 'media')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'WARNING').strip().upper()
LOG_DIR = os.path.join(SITE_DIR, 'log')
STATICFILES_FINDERS = (
    # http://djbook.ru/examples/33/
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
ADMIN_MEDIA_PREFIX = '/static/admin/'
# https://docs.djangoproject.com/en/2.1/ref/settings/#append-slash

LOG_FORMAT = (
    'DJANGO: %(asctime)s |'
    # '%(thread)s |'
    # '[ %(pathname)-110s ]'
    '%(module)-20s '  # python.module.path
    'line:%(lineno)4d | '  # code line-number
    'fn: %(funcName)-20s '
    '| %(name)-25s '                    # logging-name
    '%(levelname)-7s'
    ' :    %(message)s'
)
LOG_DATE_FORMAT = '%m.%d %H:%M:%S'


# https://docs.djangoproject.com/en/2.1/topics/logging/#examples
# https://lincolnloop.com/blog/django-logging-right-way/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format':   LOG_FORMAT,
            'datefmt':  LOG_DATE_FORMAT,
        },
    },

    'handlers': {
        'console': {
            'class':        'logging.StreamHandler',
            'level':        'DEBUG',
            'formatter':    'verbose'
        },
    },

    'loggers': {
        '': {
            'handlers':     [
                'console',
                'sentry',
            ],
            'level':        LOG_LEVEL,
            'propagate':    False,
        },
        # - - -
        'django':           {'level': 'WARNING', 'propagate': False, 'handlers':['console', 'sentry', ]},
        'django.request':   {'level': 'WARNING', 'propagate': False, 'handlers':['console', 'sentry', ]},
        # - - -
        'app_leads':        {'level': 'DEBUG',   'propagate': False, 'handlers':['console', 'sentry', ]},
        'app_common':       {'level': 'DEBUG',   'propagate': False, 'handlers':['console', 'sentry', ]},
    },
}

# ------------------------------------------------------------------------------
SITE_ID = 1



