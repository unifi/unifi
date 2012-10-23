#!/usr/bin/env python2.7
# -*- coding: utf8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from login.util import Client
from unifi.management import UserManager



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

        context = {
            'title':    title,
            'message':  message,
            'set':      collection,
        }

        return render( self.request, "dialog.html", context );


    def error( self ):
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
        self.person = UserManager.getPerson( self.user.username )
        
        if self.request.user.is_authenticated():
            return self.allow( *args, **kwargs )
        else:
            return self.deny()


    def deny( self ):
        client = Client( self.request )

        if client.is_banned():
            return HttpResponse( status=403 )
        else:
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





class ModelView( AccessRestrictedView ):
    """
    Please, don't use this.
    """

    def __init__( self, model=None ):
        self.model = model

    def allow( self, pk ):
        if self.request.method == "DELETE":
            try:
                target = self.model.objects.get( pk=pk )
                target.delete()
            except ValueError, ObjectDoesNotExist:
                return HttpResponse( status=404 )

