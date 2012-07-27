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

        from random import sample

        # assistance_groups = sample( list( Group.objects.all() ), 10 )

        # for g in assistance_groups:
            # g.needs_assistance = True
            # g.save()

        assistance_groups = Group.objects.filter( needs_assistance=True )

        wishes = Wish.objects.filter( student=student )
        wishes = [w for w in wishes if w.is_active]

        groups = Group.objects.filter( students__in=[student] )

        autocomplete = Tag.objects.all()

        def tag_distribution():
            return {
                "brick": 20,
                "guatemalan": 30,
                "replace": 40,
                "chair": 70,
                "estimate": 10,
                "afternoon": 5,
                "feature": 1,
                "slope": 10,
                "spider": 15,
                "colt": 25,
                "pediatrician": 37,
                "mosquito": 14,
                "asdfasfd": 12,
                "masonry": 10,
            }

        from unifi.management import UserManager

        # for u in sample( list(Student.objects.all()), 10 ):
            # UserManager.updateUser( u.username(), "o" )

        is_oracle = False
        if UserManager.getOracle( request.user.username ) != None:
            is_oracle = True


        return render_to_response( "my/index.html", {
                "title":                "UNIFI",
                "groups":               groups,
                "wishes":               wishes,
                "assistance_groups":    assistance_groups,
                "autocomplete":         tag_distribution(),
                "is_oracle":            is_oracle,
            },
            context_instance = RequestContext( request )
        )

    else:
        return redirect( "/" )


def wish_delete( request, pk ):
    """
    Removes a wish from the database and the existing matching graph.
    @param pk:    public key of the wish to remove
    """

    if request.user.is_authenticated:
        student = UserManager.getStudent( request.user.username )

        try:
            w = Wish.objects.get(pk=pk)
            WishDispatcher.delete_wish_from_graph(w)
            Wish.objects.get( pk=pk ).delete()
        except ObjectDoesNotExist, ValueError:
            print "-> Client attempted deleting a non-existing record"

    return redirect( "/" )
