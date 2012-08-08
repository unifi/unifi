# -*- coding: utf8 -*-

from unifi.management import GroupManager
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
        print self.member, self.group.students.all()
        if self.member in self.group.students.all():
            self.group.students.remove( self.member )
            self.group.save()
            return HttpResponse( status=200 )
        else:
            return HttpResponse( status=404 )

    def post( self ):
        return HttpResponse( status=403 )

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
        
        
class Leave( AccessRestrictedView ):
    
    def allow( self, pk ):
        
        # find out whether the group is there
        try:
            group = Group.objects.get( pk=pk )
        except ObjectDoesNotExist:
            return redirect( "/" )
        
        
        # find the user
        candidates = group.students.filter( 
            user__pk=self.user.pk
        )
        
        # if user is a member of the group
        if len( candidates ) > 0:
            group.students.remove( self.user )
            group.save()
        
            return self.dialog( 
                message      = "User was removed from group",
                collection   = group.students.all()
            )
            
        else:
            return self.dialog( 
                message     = "User is not a member of the given group",
                collectin   = group.students.all()
            )        
        
        
        