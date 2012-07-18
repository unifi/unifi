#!/usr/bin/env python2.7
# -*- coding: utf8 -*-
from django.core.exceptions import ImproperlyConfigured
import sys
from util import get_project_models_dict
from os import system, getcwdu


names = get_project_models_dict().keys()
names = set([ n.lower() for n in names ])

DEBUG = False

print names
print "Working in %s" % getcwdu()
print "This script should be ran only from the root directory" + \
        "of a django project that has South-application enabled"

print "What sort of migration do you want to perform?"
choice = raw_input( "0: initial \n1: auto \n:" )

if choice is "0":

    print "Remember to DROP all tables in the database prior to running this script"
    if DEBUG:
        raw_input( "<press enter to continue>" )

    system( "./manage.py syncdb" )

    for name in names:

        # remove the folder containing migrations
        system( "rm -r ./%s/migrations/" % name )

        if DEBUG:
            raw_input( "<press enter to continue>" )

        # perform the initial migration
        system( "./manage.py schemamigration %s --initial" % name )
        system( "./manage.py migrate %s --delete-ghost-migrations" % name )

        if DEBUG:
            raw_input( "<press enter to continue>" )

elif choice is "1":

    for name in names:
        if DEBUG:
            raw_input( "<press enter to continue>" )

        # perform the initial migration
        system( "./manage.py schemamigration %s --auto" % name )
        system( "./manage.py migrate %s" % name )

        if DEBUG:
            raw_input( "<press enter to continue>" )

else:
    sys.exit(0)


