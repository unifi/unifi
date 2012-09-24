#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.db import models
from tag.models import Tag


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
