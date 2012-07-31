#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.views.generic.base import TemplateView

class UnifiView( TemplateView ):
    def __call__( self, request, *args, *kwargs ):
        self.user = request.user
        self.get()


class AccessRestrictedView( UnifiView ):
    
    def __call__( self, request, *args, **kwargs ):

        self.user = self.request.user

        if self.user.is_authenticated():
            return self.get()
        else:
            return self.get_not_authenticated()


    def get_not_authenticated( self ):
        return render_to_response( "dialog.html", {
                "title": "Not Authenticated",
                "message": "This is a the default page for users without login record.",
            },
            context_instance = RequestContext( self.request )
        )



class DefaultUnifiView( AccessRestrictedView )


if __name__ == "__main__":
    pass