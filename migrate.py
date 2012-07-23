#!/usr/bin/env python2.7
# -*- coding: utf8 -*-
from django.core.exceptions import ImproperlyConfigured
import sys
from os import system, getcwdu

from util import get_project_models_dict
from unifi.settings import INSTALLED_APPS


# names = get_project_models_dict().keys()
# names = set([ n.lower() for n in names ])

names = [
    n for n in INSTALLED_APPS
    if not n.startswith("django")
]

DEBUG = True

print names
print "Working in %s" % getcwdu()
print "This script should be ran only from the root directory" + \
        "of a django project that has South-application enabled"

print "What sort of migration do you want to perform?"
choice = raw_input( "0: initial \n1: auto \n:" )

if choice is "0":

    print "Dropping all tables"
    system( "./manage.py reset %s" )

    system( "./manage.py syncdb" )

    if DEBUG:
        raw_input( "<press enter to continue>" )

    # system( "./manage.py syncdb" )

    for name in names:

        # remove the folder containing migrations
        system( "rm -r ./%s/migrations/" % name )

        # perform the initial migration
        system( "./manage.py schemamigration %s --initial" % name )
        system( "./manage.py migrate %s --delete-ghost-migrations" % name )

        if DEBUG:
            raw_input( "<press enter to continue>" )

elif choice is "1":

    for name in names:

        # perform the initial migration
        system( "./manage.py schemamigration %s --auto" % name )
        system( "./manage.py migrate %s" % name )

        if DEBUG:
            raw_input( "<press enter to continue>" )


else:
    sys.exit(0)


