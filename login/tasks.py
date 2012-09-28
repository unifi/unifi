#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from celery.task import PeriodicTask
from datetime import timedelta
from login.util import Banned

class RegularUnban(PeriodicTask):
    run_every = timedelta( hours=1 )

    def run( self ):
        Banned.objects.all().delete()