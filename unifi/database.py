import os
PROJECT_ROOT    = os.path.dirname(
    os.path.abspath(__file__ + "/..")
)

DATABASES = {
    'default-sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_ROOT + '/kgen_utv',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'kgen_utv',
        'USER':     'kgen_utv',
        'PASSWORD': '8NBtWKn',
        'HOST':     '127.0.0.1',
        'PORT':     '5432',
    },
    'default-uio': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'kgen_utv',
        'USER':     'kgen_utv',
        'PASSWORD': '8NBtWKn',
        'HOST':     'postgres.ifi.uio.no',
        'PORT':     '113',
    },
}