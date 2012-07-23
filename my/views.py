# -*- coding: utf8 -*-
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext

from group.models import Group
from student.models import *
from unifi.management import UserManager, WishManager
from match.algorithms import *



def index( request ):

    """
    Presents an authenticated user's state in the system: the related objects.
    """

    candidates = Student.objects.filter( user=request.user )

    if len(candidates) == 0:
        student = None
    else:
        student = candidates[0]


    if request.user.is_authenticated():

        wishes = Wish.objects.filter( student=student )
        groups = Group.objects.filter( students__in=[student] )
        autocomplete_tags = Tag.objects.all()

        return render_to_response( "my/gateway.html", {
                "title":                "UNIFI",
                "groups":               groups,
                "wishes":               wishes,
                # "assistance_wishes":    Wish.objects.filter( needs_assistance=True ),
                "autocomplete_tags":    autocomplete_tags,
            },
            context_instance = RequestContext( request )
        )

    else:
        return redirect( "/" )


def wish_delete( request, pk ):

    if request.user.is_authenticated:
        student = UserManager.getStudent( request.user.username )

        try:
            w = Wish.objects.get(pk=pk)
            WishDispatcher.delete_wish_from_graph(w)
            Wish.objects.get( pk=pk ).delete()
        except ObjectDoesNotExist, ValueError:
            print "-> Client attempted deleting a non-existing record"

    return redirect( "/" )
