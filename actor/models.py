# -*- coding: utf8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db import models
from tag.models import Tag


class Group( models.Model ):

    tags = models.ManyToManyField( Tag, null=True )
    slots = models.ManyToManyField( "Slot" )



class Slot( models.Model ):

    person = models.ForeignKey( "Person", null=True )
    role = models.ForeignKey( "Role", null=False )
    is_leader = models.BooleanField( default=False )


    # operations
    def clear( self ):
        pass

    # non-unique field filters
    @staticmethod
    def by_role( role ):
        return Slot.objects.filter( role=role )

    @staticmethod
    def by_person( person ):
        return Slot.objects.filter( person=person )

    @staticmethod
    def empty_objects():
        return Slot.objects.filter( person=None )

    @staticmethod
    def taken_objects():
        return Slot.objects.exclude( person=None )



class Person( models.Model ):

    user = models.ForeignKey( User, unique=True )
    roles = models.ManyToManyField( "Role" )


    def get_username( self ):
        return self.user.username

    def get_slots( self ):
        return Slot.objects.filter( person=self )

    # unique field filters
    @staticmethod
    def by_user( self, user ):
        return Person.objects.get( pk=user.pk )

    @staticmethod
    def by_username( self, username ):
        return Person.objects.get( username=username )

    # non-unique field filters
    @staticmethod
    def by_role( self, role ):
        return Person.objects.filter( roles__in=[role] )



class Role( models.Model ):

    name = models.CharField( max_length=50, unique=True )


    # unique field filters
    @staticmethod
    def by_name( name ):
        return Role.objects.get( name=name )

    # non-unique field filters
    def get_persons( self ):
        return Person.objects.filter( roles__in=[self] )

    def get_slots( self ):
        return Slot.objects.filter( role=self )











#    Actor.objects.get( user=user )
#    Role.objects.get( name="Student" )
#    Actor.objects.filter( roles__in=[role] )


class Actor( models.Model ):

    user = models.ForeignKey( User )
    roles = models.ManyToManyField( Role )

class Alias( models.Model ):
    pass