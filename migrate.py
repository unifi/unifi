#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

import sys
from os import system, getcwdu, environ
from shutil import rmtree
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
        'initial': "0",
        'auto'   : "1",
    }

    names = get_applications(
        INSTALLED_APPS,
        exclude=[ "django", "debug", "south" ]
    )

    choice_prompt( choices )
    choice = raw_input()

    if choice is choices['initial']:

        drop_database()
        system( "python manage.py syncdb --all" )

        breakpoint()

        for name in names:
            rmtree( "./%s/migrations/" % name )
            system( "python manage.py schemamigration %s --initial" % name )
            breakpoint()

        system( "python manage.py migrate" )

    elif choice is choices['auto']:
        for name in names:
            system( "python manage.py schemamigration %s --auto" % name )
            breakpoint()
        system( "python manage.py migrate" )

    else:
        sys.exit(0)