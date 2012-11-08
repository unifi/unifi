#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.db import models
from django_extensions.db.models import TimeStampedModel
from person.models import Person, Wish
from unifi.rules import GROUP_CAPACITY, GOAL_TEXT_LENGTH


class Group( TimeStampedModel ):
    """
    Contains Person objects, has a flag that identifies an assistance request.
    Number of group members is limited by its capacity, yet a group that is
    full accepts new members if it has open slots.
    """
    wishes           = models.ManyToManyField( Wish )
    persons          = models.ManyToManyField( Person, null=True )
    needs_assistance = models.BooleanField() # deprecate when slots are introduced, represent as an expert slot
    capacity         = models.IntegerField( default=GROUP_CAPACITY ) # bypassed via slots
    slots            = models.ManyToManyField( "Slot", null=True )
    is_announced     = models.BooleanField()
    goal             = models.CharField( max_length=GOAL_TEXT_LENGTH, null=True, default="" )
    description      = models.TextField( null=True )


    def age( self ):
        from django.utils.timezone import now
        return ( now() - self.created ).total_seconds()

    def add_wish( self, wish ):
        self.wishes.add( wish )
        self.persons.add( wish.person )

    def remove_person( self, person ):
        #[!] test
        self.persons.filter( person_pk=person.pk ).delete()
        self.wishes.filter( person=person ).delete()

    # [!] returns a QuerySet
    def tags( self ):
        """
        Return group tags as a models.query.QuerySet
        """
        wishes = self.wishes.all()
        tags = wishes[0].tags.all()
        for wish in wishes[1:]:
            tags = tags | wish.tags.all()

        return tags.distinct()


    def uncommon_tags( self ):
        result = set( self.tags() ).difference( self.common_tags() )
        return result

    # [!] returns a set
    def common_tags( self ):
        result = set()
        for w in self.wishes.all():
            wish_tags = set( w.tags.all() )
            if len(result) > 0:
                result.intersection_update( set( w.tags.all() ) )
            else:
                result = wish_tags
        return sorted( result, key=lambda x: x.name )


    def is_open( self ):
        return self.persons.count() < self.capacity

    def contact( self, message ):
        from django.core.mail import EmailMessage, get_connection
        email = EmailMessage()
        email.body = message
        email.subject = "[UNIFI]"
        email.connection = get_connection()
        for person in self.persons.all():
            print "{0}({1})".format(person.username(), person.pk)
            address = person.user.email
            if address:
                email.cc.append( person.user.email )
        print message
        email.send()


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
    role        = models.ForeignKey( "Role", null=False )
    person      = models.ForeignKey( Person, null=True, related_name="person" )
    candidates  = models.ManyToManyField(
        Person, null=True, related_name="candidates" )

class Role( models.Model ):
    """
    Describes a Person's rights and properties as a member of a group or inside
    the system. In other words, it can be used as an indication of what a person
    can do and what that person needs to see (of the state representation)
    ...
    Ex. an 'expert' is predominantly used to assist regular group members, or
    to lead a project that a group is commited to.
    """
    name        = models.CharField( max_length=50, null=False, unique=True )