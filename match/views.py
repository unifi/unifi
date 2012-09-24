# -*- coding: utf8 -*-

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from core.views import AccessRestrictedView
from student.models import Wish
from util import *


class Match( AccessRestrictedView ):

    def allow( self ):

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
            context_instance = RequestContext( self.request )
        )