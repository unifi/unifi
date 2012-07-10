#!/usr/bin/env python2.7

from getpass import getpass

engine_choice = raw_input(
"""Choose database type from the list:
1. postgresql
2. sqlite (default)
""" )


if engine_choice == "1":
    engine = "django.db.backends.postgresql_psycopg2"
    
    template = \
"""
DATABASES = {
    '%s': {
        'ENGINE':   '%s',
        'NAME':     '%s',
        'USER':     '%s',
        'PASSWORD': '%s',
        'HOST':     '%s',
        'PORT':     '%s',
    },
}
""" % (
        "default",
        engine,
        raw_input( "Specify database name: \n" ),
        raw_input( "Specify username: \n" ),
        getpass  ( "Specify password: \n" ),
        raw_input( "Specify host: \n" ),
        raw_input( "Specify port (ex. 5432): \n", )
    )    
    
    
elif engine_choice == "2":
    engine = "django.db.backends.sqlite3"
    
    template = \
    """
import os
PROJECT_ROOT = os.path.dirname(
    os.path.abspath( __file__ + "/.." )
)

DATABASES = {
    '%s': {
        'ENGINE':   '%s',
        'NAME':     %s,
        'USER':     '%s',
        'PASSWORD': '%s',
        'HOST':     '%s',
        'PORT':     '%s',
    },
}
""" % (
        "default",
        engine,
        "PROJECT_ROOT + '/sqlite.db'",
        "",
        "",
        "",
        ""
    )

import os.path

if raw_input( "Store the configuration as database.py? (y/n) " ) == "y":
    with open( "database.py", "w" ) as out:
        out.write( template.strip() )
    
