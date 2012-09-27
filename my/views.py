# -*- coding: utf8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from core.views import AccessRestrictedView
from unifi.management import UserManager
from group.models import Group
from person.models import *
from unifi.management import UserManager


from django import template


class MyView( AccessRestrictedView ):

    def allow( self ):

        candidates = Person.objects.filter(
            user=self.request.user
        )

        if len(candidates):
            person = candidates[0]
        else:
            person = None


        if self.request.user.is_authenticated():

            # assistance_groups = sample( list( Group.objects.all() ), 10 )

            # for g in assistance_groups:
                # g.needs_assistance = True
                # g.save()

            assistance_groups = Group.objects.filter( needs_assistance=True )

            wishes = Wish.objects.filter( person=person )
            wishes = [ w for w in wishes if w.is_active ]

            groups = Group.objects.filter( persons__in=[person] )

            autocomplete = Tag.objects.all()

            # for u in sample( list(Person.objects.all()), 10 ):
                # UserManager.updateUser( u.username(), "o" )

            return render_to_response( "my/index.html", {
                    "title":                "UNIFI",
                    "groups":               groups,
                    "wishes":               wishes,
                    "assistance_groups":    assistance_groups,
                },
                context_instance = RequestContext( self.request )
            )

        else:
            return redirect( "/" )


class Handlebars( AccessRestrictedView ):

    def allow( self ):

        return render_to_response( "my/handlebars.html", {
                "title":                "UNIFI",
            },
            context_instance = RequestContext( self.request )
        )

class WishView( AccessRestrictedView ):

    def allow( self ):

        person = Person.objects.get( user=self.user )
        wishes = Wish.objects.filter( person=person )

        return render_to_response( "wish/wishes.html", {
                "wishes": wishes,
                "delete": 1
            },
            context_instance = RequestContext( self.request )
        )

class GroupView( AccessRestrictedView ):

    def allow( self ):

        person = Person.objects.get( user=self.user )
        groups = Group.objects.filter( persons__in=[person] )

        return render_to_response( "group/groups.html", {
                "groups": groups,
                "controls": 1
            },
            context_instance = RequestContext( self.request )
        )

class AssistanceView( AccessRestrictedView ):

    def allow( self ):
        groups = Group.objects.filter( needs_assistance=True )

        return render_to_response( "group/groups.html", {
                "groups": groups,
            },
            context_instance = RequestContext( self.request )
        )