from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from student.models import Wish, Student
from tag.models import Tag

from util import *

def match( request ):

    all_tags = []
    for wish in Wish.objects.all():
        all_tags += list( wish.tags.all() )

    unique_tags = set( all_tags )

    lonely_tags = []
    for tag in unique_tags:
        if all_tags.count( tag ) == 1:
            lonely_tags.append( tag )
            print "lonely: %s" % tag



    wishes = Wish.objects.exclude( tags__in=lonely_tags )

    print wishes.count()

    pool = Pool( wishes )
    pairs = sorted( list(pool.pair() ), key=lambda x: x[0], reverse=True )

    return render_to_response( "match.html", {
            "title":    "Matching",
            "message":  "Displaying %d pairs" % len(pairs),
            "matches":  pairs
        },
        context_instance = RequestContext( request )
    )


def default_match( request ):

    all_tags = []
    for wish in Wish.objects.all():
        all_tags += list( wish.tags.all() )

    unique_tags = set( all_tags )

    lonely_tags = []
    for tag in unique_tags:
        if all_tags.count( tag ) == 1:
            lonely_tags.append( tag )
            print "lonely: %s" % tag



    wishes = Wish.objects.exclude( tags__in=lonely_tags )

    print wishes.count()

    pool = Pool( wishes )
    pairs = sorted( list(pool.pair() ), key=lambda x: x[0], reverse=True )

    return render_to_response( "match.html", {
            "title":    "Matching",
            "message":  "Displaying %d pairs" % len(pairs),
            "matches":  pairs
        },
        context_instance = RequestContext( request )
    )

def graph_match( request ):

    # [+] add graph based matching and remap the urls.py to it

    return redirect( "." )