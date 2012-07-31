#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.views.generic.base import TemplateView

class AccessRestrictedView( TemplateView ):

    def __call__( self, request, *args, **kwargs ):

        self.request = request
        self.user = self.request.user

        if self.request.user.is_authenticated():
            return self.authenticated( *args, **kwargs )
        else:
            return self.not_authenticated()


    def not_authenticated( self ):
        return render_to_response( "dialog.html", {
                "title": "Not Authenticated",
                "message": \
                  "This is a the default page for users without login record.",
            },
            context_instance = RequestContext( self.request )
        )




if __name__ == "__main__":
    pass