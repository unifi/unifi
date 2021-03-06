# -*- coding: utf8 -*-

from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel

from unifi.rules import WISH_EXPIRATION_DAYS
from person.managers import WishManager
from tag.models import Tag

from datetime import date
from dateutil.relativedelta import relativedelta


class Person( models.Model ):

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

    def wishes( self ):
        return Wish.objects.filter( person=self )

    def groups( self ):
        from group.models import Group
        return Group.objects.filter( persons__in=[self] )




class Wish( TimeStampedModel ):
    objects = WishManager()

    person = models.ForeignKey( Person )
    tags = models.ManyToManyField( Tag )
    is_active = models.BooleanField( default=True )
    expires = models.DateField(
        default=( date.today() + relativedelta( days=WISH_EXPIRATION_DAYS ) )
    )

    def groups( self ):
        from group.models import Group
        return Group.objects.filter( wishes__in=[self] )

    def age( self ):
        from django.utils.timezone import now
        return ( now() - self.created ).total_seconds()

    def __unicode__( self ):
        return "Wish: " + self.person.__unicode__()


