
# -*- coding: utf8 -*-

from django.http import HttpResponse
from group.models import Group
from core.views import *
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

    def get( self, group ):
        response = self.dialog(
            title = group,
            message = "The group has following members",
            collection = group.persons.all()
        )

    def post( self, group ):

        user = self.request.user
        person = UserManager.getPerson( user.username )

        if self.request.POST.get( "needs_assistance" ):
            if group.persons.filter(pk=person.pk):
                if group.needs_assistance:
                    group.needs_assistance = False
                else:
                    group.needs_assistance = True

                group.save()

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

            # considering the objects are found
            if self.request.method == "GET":
                response = self.get()
            elif self.request.method == "DELETE":
                response = self.delete()

        except ObjectDoesNotExist, ValueError:
            # objects not found, thus can be created
            if self.request.method == "PUT":
                response = self.put()
            elif self.request.method == "POST":
                response = self.post()

        return response


    def get( self ):
        return HttpResponse( status=200 )


    def delete( self ):
        member = self.member
        group = self.group

        if member in group.persons.all():
            group.persons.remove( member )

            if not group.persons.count():
                group.delete()
            else:
                group.save()

            return HttpResponse( status=200 )
        else:
            return HttpResponse( status=410 )

    def post( self ):
        return HttpResponse( status=501 )

    def put( self ):
        self.group.persons.add( self.member )
        self.group.save()
        return HttpResponse( status=200 )



class All( AccessRestrictedView ):

    def allow( self ):
        groups = Group.objects.all()

        return render_to_response( "group/all.html", {
                'standalone':   True,
                'title':        "All groups",
                'groups':       groups,
            },
            context_instance = RequestContext( self.request )
        )

class Inspect( AccessRestrictedView ):
    
    def allow( self, pk ):
        try:
            group = Group.objects.get( pk=pk )
        except ObjectDoesNotExist:
            return self.dialog(
                message = "No group with such id was found"
            )
        
        return self.dialog(
            title = group,
            message = "The group has following members",
            collection = group.persons.all()
        )
















