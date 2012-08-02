#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
import unifi


class UnifiView:

    def dialog( self, title="", message="", set=None ):
        """ 
            A shorthand for the dialog template. 
            'dialog.html' is a generic template that displays various data
            and takes three agruments, just like this function.
            
            @param title    the title to be placed in the title-tag.
            @param message  the textual part of the dialog
            @param set      a collection to be represented as a list in the
                            dialog
        """
        
        return render_to_response( "dialog.html", {
                'title':    title,
                'message':  message,
                'set':      set,
            },
            context_instance = RequestContext( self.request )
        )

class AccessRestrictedView( UnifiView ):

    def __call__( self, request, *args, **kwargs ):
    
        self.request = request
        self.args = args
        self.kwargs = kwargs
        self.user = self.request.user
        
        if self.request.user.is_authenticated():
            return self.authenticated( *args, **kwargs )
        else:
            return self.not_authenticated()


    def not_authenticated( self ):
        return render_to_response( "dialog.html", {
                "title": "Not Authenticated",
                "message": \
                    "Velkommen til UNIFI, du er ikke pålogget. " + \
                    "For å logge deg på benytt universitetets" + \
                    "innloggingsportal."
            },
            context_instance = RequestContext( self.request )
        )




class DevelopmentOnlyView( UnifiView ):

    def __call__( self, request, *args, **kwargs ):

        self.request = request
        self.args = args
        self.kwargs = kwargs
        self.user = self.request.user

        from unifi.settings import DEBUG

        if DEBUG:
            return self.allow( *args, **kwargs )
        else:
            return self.deny()


    def deny( self ):
        return render_to_response( "dialog.html", {
                "title": "Development is over",
                "message": "This page is restricted to development phase."
            },
            context_instance = RequestContext( self.request )
        )
        
        
    
        