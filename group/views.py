# -*- coding: utf8 -*-

from django.http import HttpResponse
from group.models import Group
from core.views import *
from unifi.management import UserManager

class Select( AccessRestrictedView ):

    def allow( self, pk ):
        response = HttpResponse( status = 200 )

        try:
            group = Group.objects.all( pk=pk );

            if self.request.method == "GET":
                response = self.dialog(
                    title = group,
                    message = "The group has following members",
                    collection = group.students.all()
                )
        except ObjectDoesNotExist, ValueError:
            response = self.dialog(
                message = "No group with such id was found"
            )

        return response



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
                self.member = UserManager.getStudent(
                    self.request.user.username
                )
            else:
                self.member = self.group.students.get( pk=member_pk )

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

        if member in group.students.all():
            group.students.remove( member )

            if not group.students.count():
                group.delete()
            else:
                group.save()

            return HttpResponse( status=200 )
        else:
            return HttpResponse( status=410 )

    def post( self ):
        return HttpResponse( status=501 )

    def put( self ):
        self.group.students.add( self.member )
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
            collection = group.students.all()
        )
        