# -*- coding: utf8 -*-

from os.path import dirname, realpath, basename
from database import DATABASES
import djcelery



DEBUG = False
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = dirname(
    realpath( __file__ + "/../" )
)

# TEMPLATE_DIRS = ( PROJECT_ROOT + '/templates', )

TEMPLATE_DIRS = (
    "/home/ilyakh/webapps/unifi/myproject/templates/",

)
# ( PROJECT_ROOT + '/templates/', )



# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # Use PROJECT_ROOT if you store the target files in the project folder.
    #PROJECT_ROOT + "/static_base/",
    "/home/ilyakh/webapps/unifi/myproject/static_base/",
)

if DEBUG: # Load reduction measure
    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.SHA1PasswordHasher',
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )



ADMINS = ()

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Oslo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'nb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# Use PROJECT_ROOT if you store the target files in the project folder.
STATIC_ROOT = '/home/ilyakh/webapps/unifi_static/'
# PROJECT_ROOT + '/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
# STATIC_URL = '/static/'
STATIC_URL = '/static/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'qm1=rh=r-#1dqu2_&amp;8ci#zlpi3l82d+&amp;6^$y1kxki7c#0roa5h'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'unifi.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'unifi.wsgi.application'


##

INSTALLED_APPS = (
    # third party applications
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'debug_toolbar',
    'rest_framework',
    'djsupervisor',
    # socialregistration
    'socialregistration',
    'socialregistration.contrib.openid',
    'socialregistration.contrib.twitter',
    'socialregistration.contrib.github',
    #
    'django_extensions',
    'djcelery',
    'kombu.transport.django', # celery broker
    # model-specific applications
    'person', # contains 'wish'
    'group',
    'tag',
    # control-specific applications
    'match',
    # 'prototype',
    'util',
    # 'util' candidates
        'login',
        'communication',
    # information aggregator applications
    'my',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'socialregistration.contrib.openid.auth.OpenIDAuth',
    'socialregistration.contrib.twitter.auth.TwitterAuth',
    'socialregistration.contrib.github.auth.GithubAuth',
)

TWITTER_CONSUMER_KEY = 'eLBZ5EytNpE5vBotKKz6g'
TWITTER_CONSUMER_SECRET_KEY = 'x8ZjrcklM3M3XxxqIyDbitgpPLkdFDrO6nY96LPtaos'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

DEBUG_TOOLBAR_PANELS = (
     'debug_toolbar.panels.version.VersionDebugPanel',
     'debug_toolbar.panels.timer.TimerDebugPanel',
     'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
     'debug_toolbar.panels.headers.HeaderDebugPanel',
     'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
     'debug_toolbar.panels.template.TemplateDebugPanel',
     'debug_toolbar.panels.sql.SQLDebugPanel',
     'debug_toolbar.panels.signals.SignalDebugPanel',
     'debug_toolbar.panels.logger.LoggingPanel',
 )

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

INTERNAL_IPS = (
    '127.0.0.1',
)

#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

SITE_ID = 1

# Celery: asynchronous stack queue used in matching and heavy optimization
djcelery.setup_loader()

BROKER_URL = 'django://'
CELERYD_CONCURRENCY = 1

# Email-backend: dumps the contents of email messages into the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_URL = "/"
LOGIN_REDIRECT_URL = "/my/"
LOGOUT_URL = "/login/leave"

SOCIALREGISTRATION_SETUP_FORM = "login.forms.UserForm"

CELERY_ALWAYS_EAGER = True

# Name of nodes to start, here we have a single node
CELERYD_NODES="worker1"

# Where to chdir at start.
CELERYD_CHDIR="/home/ilyakh/webapps/unifi/myproject/"

# How to call "manage.py celeryd_multi"
CELERYD_MULTI="$CELERYD_CHDIR/manage.py celeryd"

# How to call "manage.py celeryctl"
CELERYCTL="$CELERYD_CHDIR/manage.py celeryctl"

# Extra arguments to celeryd
CELERYD_OPTS="--time-limit=300 --concurrency=1"

# Name of the celery config module.
CELERY_CONFIG_MODULE="celery"

# %n will be replaced with the nodename.
CELERYD_LOG_FILE="/home/ilyakh/webapps/unifi/myproject/celery/logs/celery_%n.log"
CELERYD_PID_FILE="/home/ilyakh/webapps/unifi/myproject/celery_%n.pid"

# Workers should run as an unprivileged user.
CELERYD_USER="celery"
CELERYD_GROUP="celery"
