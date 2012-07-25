from os.path import dirname, realpath, basename
from database import DATABASES



DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = dirname(
    realpath( __file__ + "/../" )
)

# TEMPLATE_DIRS = ( PROJECT_ROOT + '/templates', )

TEMPLATE_DIRS = ( PROJECT_ROOT + '/unifi-templates', )

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# Use PROJECT_ROOT if you store the target files in the project folder.
STATIC_ROOT = PROJECT_ROOT + '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # Use PROJECT_ROOT if you store the target files in the project folder.
    PROJECT_ROOT + "/static_base/",
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
LANGUAGE_CODE = 'no'

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

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
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
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'unifi.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'unifi.wsgi.application'

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
    'south',
    # model-specific applications
    'student', # contains 'wish'
    'group',
    'oracle',
    'tag',
    # control-specific applications
    'match',
    'prototype',
    'util',
    # 'util' candidates
        'login',
        'communication',
    # information aggregator applications
    'my',
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


# Use console backend for testing
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

