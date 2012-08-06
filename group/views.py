# -*- coding: utf8 -*-

from django.shortcuts import render_to_response, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.template.context import RequestContext
from core.views import AccessRestrictedView
from group.models import Group

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
        
        
        