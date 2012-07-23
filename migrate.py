#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

import sys
from os import system, getcwdu, environ
from unifi.settings import INSTALLED_APPS


DEBUG = True
environ['DJANGO_SETTINGS_MODULE'] = 'unifi.settings'

def drop_database( username="unifi"):
    system( "psql -U postgres -c 'DROP DATABASE IF EXISTS \'unifi\';'" )
    system( "psql -U postgres -c 'CREATE DATABASE \'unifi\' OWNER \'unifi\';'" )


def get_applications( installed_apps, exclude=[], include=[] ):
    application_names = include
    for app_name in installed_apps:
        is_excluded = False
        for e in exclude:
            if e in app_name:
                is_excluded = True

        if ( app_name not in exclude ) and not is_excluded:
            application_names.append( app_name )

    return application_names

def breakpoint( message="<press enter to continue>" ):
    if DEBUG:
        raw_input(message)


def choice_prompt( choices ):
    sorted_choices = sorted( choices.items(), key=lambda x: x[1] )
    for id,description in sorted_choices:
        print "%s: %s" % (description, id)


if __name__ == "__main__":

    choices = {
        'initial': "1",
        'auto'   : "2",
    }

    names = get_applications(
        INSTALLED_APPS,
        exclude=[ "django", "debug", "south" ]
    )

    choice_prompt( choices )
    choice = raw_input()

    if choice is choices['initial']:

        drop_database()
        system( "./manage.py syncdb" )

        breakpoint()


        for name in names:

            system( "rm -r ./%s/migrations/" % name )
            # system( "./manage.py schemamigration %s --initial" % name )
            # system( "./manage.py migrate %s --delete-ghost-migrations --fake" % name )
            breakpoint()

    elif choice is choices['auto']:
        for name in names:
            # system( "./manage.py schemamigration %s --auto" % name )
            # system( "./manage.py migrate %s" % name )
            breakpoint()

    else:
        sys.exit(0)