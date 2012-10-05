#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from core.views import AccessRestrictedView
from group.models import Group
from match.algorithms import WishDispatcher
from match.rating import jaccard
from person.models import Person, Wish
from match.util import *
from unifi import UserManager, WishManager



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



# the views that generate page elements:
# [+] create a descending class called PageElementView for the following:
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





class Search( AccessRestrictedView ):

    def allow( self ):

        # [!] TEMP

        from time import time

        t = time()

        groups = Group.objects.all()
        # [!] probably needs to be checked for age as well
        wishes = Wish.objects.filter(
            is_active=True ).filter( person=self.person )

        graph = network.Graph()

        for g in groups:
            graph.add_node( g )

        # . at this point in time all groups are in the graph, but there are
        # . no connections between them. To make connections, we introduce
        # . wishes as additional nodes and make edges with perspective groups:

        report = []

        for w in wishes:
            for g in graph.nodes():
                rating = jaccard( w.tags.all(), g.tags() )
                report.append ( "Wish %s fits well into the group %s (rated: %s) <br />%s<br />%s" % ( w, g, rating, g.tags(), w.tags.all() ) )

        print time() - t

        return self.dialog( title=( time() - t), collection=report )






class CreateWish( AccessRestrictedView ):

    def allow( self ):
        result = redirect( "/" )

        tags =  self.request.POST.getlist('user[tags][]')
        tags = [ t.encode("utf8") for t in tags ]
        tags = [ t.lower() for t in tags ]

        MAX_NUMBER_OF_TAGS = 5

        if not len( tags ):
            return self.dialog( "Error", "No tags given" )

        elif len( tags ) > MAX_NUMBER_OF_TAGS:
            return self.dialog( "Error",
                  "Your wish contains too many tags. Specify max %d tags." %\
                  MAX_NUMBER_OF_TAGS
            )

        courses = WishDispatcher.extract_course_tag( tags )

        # check if user has similar wishes

        NEW_WISH_MAX_SIMILARITY = 0.75

        has_similar = False
        existing_wishes = Wish.objects.filter( person=self.person ).filter( is_active=True )

        for w in existing_wishes:
            rating = jaccard( [t.name for t in w.tags.all()], tags )
            if rating > NEW_WISH_MAX_SIMILARITY:
                return self.dialog( "Error", "One of your existing wishes is too alike" )

        if len( courses ) > 1:
            return self.dialog( "Error", "Please specify a course" )


        person = UserManager.getPerson( self.request.user.username )

        WishManager.addWish(
            person,
            tags,
            courses
        )

        return result