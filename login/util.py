#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from login.models import Attempt, Banned
from django.db import IntegrityError
from datetime import datetime
from unifi.settings import BAN_PERIOD, MAX_LOGIN_ATTEMPTS


class Client:

    def __init__( self, request ):

        self.request = request
        self.address = self.get_address()
        self.banned = None

        # check if this client has a ban record
        try:
            self.banned = Banned.objects.get( address=self.address )
        except Banned.DoesNotExist:
            pass

        if self.banned:
            # unbans the address if the ban period has passed
            if self.banned_since() > BAN_PERIOD:
                self.unban()

        else:
            # checks whether the client needs a ban record
            # registers a failed login attempt

            failed_attempts = Attempt.objects.filter( address=self.address )
            if failed_attempts.count() > MAX_LOGIN_ATTEMPTS:
                self.ban()

    def banned_since( self ):
        return (
            datetime.now( tz=self.banned.date.tzinfo ) - self.banned.date
        ).total_seconds()

    def get_address( self ):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

    def is_banned( self ):
        return self.banned is not None

    def ban( self ):
        try:
            # blacklist the client address
            self.banned = Banned( address=self.address )
            self.banned.save()
            # remove all previous attempts from the log
            attempts = Attempt.objects.filter( address=self.address )
            attempts.delete()
            return True
        except IntegrityError:
            return False

    def unban( self ):
        try:
            banned = Banned.objects.get( address=self.address )
            banned.delete()
            self.banned = None
            return True
        except Banned.DoesNotExist:
            return False
