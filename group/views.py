#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.http import HttpResponse
from group.models import Group
from core.views import *
from person.models import Wish
from unifi.management import UserManager

class Select( AccessRestrictedView ):

    def allow( self, pk ):
        response = HttpResponse( status=200 )

        try:
            group = Group.objects.get( pk=pk )

            if self.request.method == "GET":
                response = self.get( group )

            elif self.request.method == "POST":
                response = self.post( group )

        except Group.DoesNotExist, ValueError:
            response = self.dialog(
                message = "No group with such id was found"
            )

        return response

    def get( self, group_instance ):

        group = group_instance

        context = {
            'group': group,
        }

        return render( self.request, "group/detailed.html", context )


    def post( self, group_instance ):

        user = self.request.user
        person = UserManager.getPerson( user.username )

        if self.request.POST.get( "needs_assistance" ):
            if group_instance.persons.filter(pk=person.pk):
                if group_instance.needs_assistance:
                    group_instance.needs_assistance = False
                else:
                    group_instance.needs_assistance = True

                group_instance.save()

            return HttpResponse( status=201 )



class SelectMember( AccessRestrictedView ):
    """
    Selects a member of a group for operations.
    Accessing the resource by this view allows you
    to perform ReSTful-style like operations.
    """
    def allow( self, group_pk, member_pk ):

        response = HttpResponse( status=200 )

        try: # to find the objects
            self.group = Group.objects.get( pk=group_pk )

            if member_pk == "":
                # assumes that the user is the login record
                self.member = UserManager.getPerson(
                    self.request.user.username
                )
            else:
                self.member = self.group.persons.get( pk=member_pk )


            if self.request.method == "GET":
                response = self.get()
            elif self.request.method == "DELETE":
                response = self.delete()
            elif self.request.method == "PUT":
                response = self.put()
            elif self.request.method == "POST":
                response = self.post()

        except Group.DoesNotExist, ValueError:
            return HttpResponse( status=404 )

        return response


    def get( self ):
        return HttpResponse( status=200 )


    def delete( self ):
        member = self.member
        group = self.group

        if member in group.persons.all():
            group.persons.remove( member )
            members_left = group.persons.count()
            if members_left < 2:
                # deletes the group if it has less than 2 members
                for w in group.wishes.all():
                    # and reactivates the wishes
                    w.is_active = True
                    w.save()
                group.delete()

            else:
                try:
                    w = group.wishes.get( person=member )
                    w.is_active = True
                    w.save()
                except Wish.DoesNotExist:
                    pass

                group.save()

            return HttpResponse( status=200 )
        else:
            return HttpResponse( status=410 )

    def post( self ):
        return HttpResponse( status=501 )

    def put( self ):
        if self.person in self.group.persons.all():
            # the user is already a member of a group
            return HttpResponse( status=412 )

        if self.group.persons.count() >= self.group.capacity:
            # the group is over capacity
            return HttpResponse( status=412 )

        self.group.persons.add( self.member )
        self.group.save()
        return HttpResponse( status=200 )




class All( AccessRestrictedView ):

    def allow( self ):
        groups = Group.objects.exclude( persons__in=[self.person] )

        context = {
            'standalone': True,
            'title': "Other groups",
            'groups': groups,
        }

        return render( self.request, "group/all.html", context );


class Inspect( AccessRestrictedView ):
    
    def allow( self, pk ):
        try:
            group = Group.objects.get( pk=pk )
        except Group.DoesNotExist:
            return self.dialog(
                message = "No group with such id was found"
            )
        
        return self.dialog(
            title = group,
            message = "The group has following members",
            collection = group.persons.all()
        )
