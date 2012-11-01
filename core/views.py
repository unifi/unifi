#!/usr/bin/env python2.7
# -*- coding: utf8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from login.util import Client
from person.models import Person
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

        return render( self.request, "dialog.html", context )


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
        
        if self.request.user.is_authenticated():

            self.user = self.request.user

            try:
                self.person = Person.objects.get( user=self.user )
            except Person.DoesNotExist:
                self.person = Person( user=self.user )
                self.person.save()

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
            return self.deny( *args, **kwargs )


    def deny( self, *args, **kwargs ):
        return self.dialog(
            title   = "Development is over. We're done. Everything is perfect.",
            message = "This page was restricted to the development phase."
        )


class MethodView( AccessRestrictedView ):

    def __init__( self, model ):
        self.model = model

    def allow( self, pk=None, *args, **kwargs ):

        self.pk = pk

        self.get = lambda a,k: HttpResponse( status=403 )
        self.post = lambda a,k: HttpResponse( status=403 )
        self.put = lambda a,k: HttpResponse( status=403 )
        self.delete = lambda a,k: HttpResponse( status=403 )

        if self.request.method == "GET":
            return self.get( self.pk, args, kwargs )
        elif self.request.method == "POST":
            return self.post( self.pk, args, kwargs )
        elif self.request.method == "PUT":
            return self.put( self.pk, args, kwargs )
        elif self.request.method == "DELETE":
            return self.delete( self.pk, args, kwargs )
        else:
            return HttpResponse( status=501 )


