#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from core.views import AccessRestrictedView, DevelopmentOnlyView


class Match( DevelopmentOnlyView ):
    """
    Temporary development matching process trigger.
    Recreated as a task/regular task in production.
    """

    def allow( self ):

        return self.dialog(
            title="Match",
            message="Not defined"
        )