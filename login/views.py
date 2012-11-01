# -*- coding: utf8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import auth
from django.shortcuts import render
from core.views import AccessRestrictedView
from login.models import Attempt
from login.util import Client
from unifi.rules import BAN_PERIOD_MINUTES



class Gateway( AccessRestrictedView ):

    def allow( self ):
        return redirect( "/my" )

    def deny( self ):

        client = Client( self.request )

        if client.is_banned():
            return HttpResponse( status=403 )
        else:
            context = {
                'title':    "UNIFI",
            }
            return render( self.request, "login/login.html", context )



class Leave( AccessRestrictedView ):

    def allow( self ):
        """
        A silent logout routine
        """
        auth.logout( self.request )
        return redirect( "socialregistration:logout" )



class Login( AccessRestrictedView ):

    def allow( self ):
        return redirect( "/my/" )

    def deny( self ):

        # fetching the provided data
        client = Client( self.request )
        username = self.request.POST.get( "username" )
        password = self.request.POST.get( "password" )

        if not password:
            return self.dialog(
                message="Your login attempt lacks password"
            )

        # see if client has had previous failed attempts to login
        failed_attempts = Attempt.objects.filter( address=client.address )

        if client.is_banned():
            return self.dialog(
                message="Your address has been blocked for further login attempts. " + \
                "Please wait %s seconds before you try again." \
                % ( BAN_PERIOD_MINUTES - client.banned_since() )
            )

        else:
            # fetching user
            user = auth.authenticate( username=username, password=password )

            # logging the user in
            if user:
                # remove all the failed attempts
                attempts = Attempt.objects.filter( address=client.address )
                if attempts.count() > 0:
                    attempts.delete()

                # create a session
                auth.login( self.request, user )
            else:
                # register a failed attempt
                attempt = Attempt(
                    address=client.address,
                    username=username
                )
                attempt.save()

            return redirect( "/" )

