# -*- coding: utf8 -*-
from django.http import HttpResponse

from django.shortcuts import redirect
from core.views import AccessRestrictedView, UnifiView
from django.contrib import auth
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from login.models import Attempt, Banned
from login.util import Client, BAN_PERIOD


class Gateway( AccessRestrictedView ):
    """
    Redirects the user to different locations, depending on whether user
    is identified or not.

    Unauthenticated users are redirected to an informative page about project's
    mission and registering process.

    Authenticated users are redirected to their personal overview (profile)

    """

    def allow( self ):
        return redirect( "/my" )

    def deny( self ):

        client = Client( self.request )

        if client.is_banned():
            return HttpResponse( status=403 )
        else:
            return render_to_response( "login/login.html",
                {
                    'title': "UNIFI",
                },
                context_instance=RequestContext(self.request)
            )

class Leave( AccessRestrictedView ):

    def allow( self ):
        """
        A silent logout routine
        """
        auth.logout( self.request )
        return redirect( "/" )

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
                % ( BAN_PERIOD - client.banned_since() )
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

