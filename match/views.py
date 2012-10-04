#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from core.views import AccessRestrictedView, DevelopmentOnlyView
from match.tasks import match_groups


class Match( DevelopmentOnlyView ):
    """
    Temporary development matching process trigger.
    Recreated as a task/regular task in production.
    """

    def allow( self ):
        match_groups()
        return self.dialog( "Matching started", "Check your page" )


