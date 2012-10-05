#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.db import models

class Attempt( models.Model ):
    """
    Stores a failed attempt to access the system with a date, and
    the information provided by user.
    """
    address = models.IPAddressField()
    username = models.CharField( max_length=60 )
    date = models.DateTimeField( auto_now_add=True )

class Banned( models.Model ):
    address = models.IPAddressField( unique=True )
    # is_permanent = models.BooleanField()
    date = models.DateTimeField( auto_now_add=True )