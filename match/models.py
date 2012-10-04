#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.db import models
from group.models import Group
from person.models import Person, Wish



class Match(models.Model):
    person = models.ForeignKey( Person, null=False )
    score = models.FloatField()

    class Meta:
        abstract = True

class GroupMatch(Match):
    group = models.ForeignKey( Group, null=False )

class WishMatch(Match):
    wish = models.ForeignKey( Wish, null=False )


# class Bucket( models.Model ):
#    name            = models.CharField( max_length=64 )
#    description     = models.TextField()
#
#    # bucket conditions
#    tags            = models.ManyToManyField( Tag, unique=True )
#    pattern         = models.TextField() # regexp
#
#    # bucket specific matching conditions
#    max_group_size  = models.IntegerField()
#    min_score       = models.DecimalField( decimal_places=2, max_digits=3  )
#    min_assistance_size \
#        = models.IntegerField()
#    wishes_per_person = models.IntegerField()
