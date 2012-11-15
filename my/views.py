# -*- coding: utf8 -*-

from django.shortcuts import render, redirect
from core.views import AccessRestrictedView
from group.models import Group
from match.rating import jaccard
from person.models import Person, Wish
from match.util import *
from unifi import UserManager, WishManager

from unifi.rules import MAX_WISHES_PER_USER, MAX_TAGS_PER_WISH, MAX_WISH_SIMILARITY

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

            assistance_groups = Group.objects.filter( needs_assistance=True )

            wishes = Wish.objects.filter( person=person )
            wishes = [ w for w in wishes if w.is_active ]

            groups = Group.objects.filter( persons__in=[person] )

            autocomplete = Tag.objects.all()

            context = {
                "title":                "UNIFI",
                "groups":               groups,
                "wishes":               wishes,
                "assistance_groups":    assistance_groups,
            }

            return self.render( "my/index.html", context )

        else:
            return redirect( "/" )



class WishView( AccessRestrictedView ):
    def allow( self ):

        person = Person.objects.get( user=self.user )
        wishes = Wish.objects.filter( person=person )

        context = {
            "wishes": wishes,
            "delete": 1
        }

        return self.render( "wish/wishes.html", context )



class GroupView( AccessRestrictedView ):
    def allow( self ):

        person = Person.objects.get( user=self.user )
        groups = Group.objects.filter( persons__in=[person] )

        context = {
            'groups': groups,
            'controls': 1
        }

        return self.render( "group/groups.html", context )



class AssistanceView( AccessRestrictedView ):
    def allow( self ):

        groups = Group.objects.filter( needs_assistance=True )

        context = {
            'groups': groups
        }

        return self.render( "group/groups.html", context )



class Search( AccessRestrictedView ):
    def allow( self ):
        return self.dialog( title="Search is not available", message="" )



class CreateWish( AccessRestrictedView ):
    def allow( self ):
        result = redirect( "/" )

        tags =  self.request.POST.getlist('user[tags][]')
        tags = [ t.encode("utf8") for t in tags ]
        tags = [ t.lower() for t in tags ]

        active_wishes = self.person.wishes().filter( is_active=True )

        if active_wishes.count() >= MAX_WISHES_PER_USER:
            return self.dialog( "Feil", "Du har altfor mange ønsker" )

        if not len( tags ):
            return self.dialog( "Feil", "Du glemte å skrive inn nøkkelord" )

        elif len( tags ) > MAX_TAGS_PER_WISH:
            return self.dialog( "Error",
                  "Du har ført inn for mange nøkkelord. Prøv å ha %d for hvert ønske." %\
                  MAX_TAGS_PER_WISH )

        def extract_course_tags( tags ):
            pattern = r'^[\-\w]+\d{4}'
            return [tag for tag in tags if re.findall(pattern, tag)]

        courses = extract_course_tags( tags )

        # check if user has similar wishes

        has_similar = False
        existing_wishes = Wish.objects.filter( person=self.person ).filter( is_active=True )

        for w in existing_wishes:
            rating = jaccard( [t.name for t in w.tags.all()], tags )
            if rating > MAX_WISH_SIMILARITY:
                return self.dialog( "Feil", "Du har et veldig likt ønske allerede. Slett det hvis du vil endre nøkkelord." )

        if len( courses ) > 1:
            return self.dialog( "Feil", "Du har angitt flere enn ett emne. Hvert ønske skal inneholde kun ett." )


        person = UserManager.getPerson( self.request.user.username )

        WishManager.addWish(
            person,
            tags,
            courses
        )

        return result