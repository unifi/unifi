# -*- coding: utf8 -*-

from django.db import models
from person.models import Wish, Person

DEFAULT_GROUP_CAPACITY = 5

class Group( models.Model ):
    """
    Contains Person objects, has a flag that identifies an assistance request.
    Number of group members is limited by its capacity, yet a group that is
    full accepts new members if it has open slots.
    """
    wishes           = models.ManyToManyField( Wish )
    persons          = models.ManyToManyField( Person, null=True )
    needs_assistance = models.BooleanField()
    capacity         = models.IntegerField( default=DEFAULT_GROUP_CAPACITY )
    slots            = models.ManyToManyField( Slot, null=True )


    def tags( self ):
        """
        Return group tags as a models.query.QuerySet
        """
        wishes = self.wishes.all()
        tags = wishes[0].tags.all()
        for w in wishes[1:]:
            tags = tags | w.tags.all()

        return tags.distinct()

    def __unicode__( self ):
        return "Group %s" % self.pk



class Slot( models.Model ):
    """
    Contains candidates and/or a chosen person that has applied for a slot in
    the group. If the group has an open slot (no 'person' assigned: hence,
    person allows null), it can accept new members even if its capacity is
    satisfied.
    ...
    A slot also identifies a 'role' of a person in the group.
    """
    role = models.ForeignKey( Role, null=False )
    person = models.ForeignKey( Person, null=True )
    candidates = models.ManyToManyField( Person, null=True )

class Role( models.Model ):
    """
    Describes a Person's rights and properties as a member of a group or inside
    the system. In other words, it can be used as an indication of what a person
    can do and what that person needs to see (of the state representation)
    ...
    Ex. an 'expert' is predominantly used to assist regular group members, or
    to lead a project that a group is commited to.
    """
    name = models.CharField( max_length=50, null=False, unique=True )