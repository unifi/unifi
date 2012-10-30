#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel

from tag.models import Tag





class Person( models.Model ):
    """ Person
    Participates in group collaboration.
    """
    user = models.ForeignKey( User, unique=True )

    def username( self ):
        return self.user.username

    def set_password( self, password ):
        self.user.set_password( password )
        self.user.save()

    def __unicode__( self ):
        return self.user.username

    def is_owner_of( self, object ):
        if isinstance( object, Wish ):
            return object.person == self
        else:
            return False

    def is_member_of( self, object ):
        from group.models import Group
        if isinstance( object, Group ):
            try:
                object.persons.get( id=self.id )
                return True
            except Person.DoesNotExist:
                return False
        else:
            return False




class Wish( TimeStampedModel ):
    person = models.ForeignKey( Person )
    tags = models.ManyToManyField( Tag )
    is_active = models.BooleanField( default=True )


    def toggle_activity( self ):
        self.is_active = not self.is_active
        self.save()

    def __unicode__( self ):
        return "Wish: " + self.person.__unicode__()


