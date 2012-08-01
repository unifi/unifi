# -*- coding: utf8 -*-

from django.shortcuts import redirect
from core.views import AccessRestrictedView

class Gateway( AccessRestrictedView ):
    """
    Redirects the user to different locations, depending on whether user
    is identified or not.

    Unauthenticated users are redirected to an informative page about project's
    mission and registering process.

    Authenticated users are redirected to their personal overview (profile)

    """

    def authenticated( self ):
        return redirect( "/my" )