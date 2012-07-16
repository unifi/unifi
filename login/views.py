# -*- coding: utf8 -*-

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext

from student.models import Student



def gateway( request ):

    """
    Redirects the user to different locations, depending on whether user
    is identified or not.

    Unauthenticated users are redirected to an informative page about project's
    mission and registering process.

    Authenticated users are redirected to their personal overview (profile)

    """

    user = request.user

    if user.is_authenticated():
        return redirect( "/my/" )
    else:
        return render_to_response( "dialog.html", {
                "title":    "UNIFI",
                "message":  """Velkommen til UNIFI, du er ikke pålogget.
                            For å logge deg på benytt universitetets
                            innloggingsportal."""
            },
            context_instance = RequestContext( request )
        )


