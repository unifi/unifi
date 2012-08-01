#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.views.generic.base import TemplateView
import unifi


class AccessRestrictedView( TemplateView ):

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




class DevelopmentOnlyView( TemplateView ):

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


