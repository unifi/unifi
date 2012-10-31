#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.db import models

from datetime import date as _date
from dateutil.relativedelta import  relativedelta

from unifi.rules import INVITATION_EXPIRATION_DAYS, MAX_INVITATION_CAPACITY



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


class Invitation( models.Model ):
    from person.models import Person

    code = models.CharField( max_length=255, unique=True )
    persons = models.ManyToManyField( Person )
    capacity = models.IntegerField( default=MAX_INVITATION_CAPACITY )
    expires = models.DateField(
        default=(
            _date.today() + relativedelta( days=INVITATION_EXPIRATION_DAYS )
        )
    )