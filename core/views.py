#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.template.context import RequestContext
import unifi


class UnifiView:

    def dialog( self, title="", message="", collection=None ):
        """ 
            A shorthand for the dialog template. 
            'dialog.html' is a generic template that displays various data
            and takes three agruments, just like this function.
            
            @param title        the title to be placed in the title-tag of the 
                                page
            @param message      the contents of the textual part of the dialog
            @param collection   a collection to be represented as a list in the
                                dialog's unordered list part
        """
        
        return render_to_response( "dialog.html", {
                'title':    title,
                'message':  message,
                'set':      collection,
            },
            context_instance = RequestContext( self.request )
        )


    def error( self ):
        """
        Not Implemented
        """
        pass

class AccessRestrictedView( UnifiView ):

    def __call__( self, request, *args, **kwargs ):
        """
        Due to security concerns, do not overload this function or
        any of its subclass overrides.
        """
    
        self.request = request
        self.args = args
        self.kwargs = kwargs
        self.user = self.request.user
        
        if self.request.user.is_authenticated():
            return self.allow( *args, **kwargs )
        else:
            return self.deny()


    def deny( self ):
        # [/] rename to 'deny'
        return self.dialog(
            
            title       = "Not Authenticated",
            message     = "Velkommen til UNIFI, du er ikke pålogget. " + \
                          "For å logge deg på benytt universitetets " + \
                          "innloggingsportal."
                          
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
        return self.dialog(
        
            title   = "Development is over. We're done. Everything is perfect.",
            message = "This page was restricted to the development phase."
            
        )
        
    

