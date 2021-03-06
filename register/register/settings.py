"""
Django settings for register project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import datetime

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOGIN_URL = '/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f9x)nfwdz@ulu$kc!k(m7xpeh#=u2m^8_hkt4lz)ajz=gkcj3n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1
PLANET = { "USER_AGENT": "OpenTaba"}
# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.admin',
)

THIRD_PARTY = (

    'pagination',
    'tagging',
    'south',
    'djcelery',
    'planet',
    'pinax_theme_bootstrap', #remove later

)

OUR_APPS = (
     'readfeed_app',
)
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY + OUR_APPS
  
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'planet.context_processors.context',
)

ROOT_URLCONF = 'register.urls'

WSGI_APPLICATION = 'register.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'he-il'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static') #where we store static files
STATIC_URL = '/static/' #what url is used to access static

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates')
    )
AUTHENTICATION_BACKENDS = ( 
    
    'django.contrib.auth.backends.ModelBackend',)
# Celery config

BROKER_URL = 'redis://localhost:6379/0'
#FEED_UPDATE_CELERY = True
CELERYBEAT_SCHEDULE = {
    #"feed-updates": {
    #  "task":"update_all_feeds",
    #  "schedule":datetime.timedelta(hours=1),
    #  }
    }

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # some other template loaders here...
)

CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

#planet config

LANGUAGE_COOKIE_NAME = "planetlng"
SESSION_COOKIE_NAME = "planetid"
