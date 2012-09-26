#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.db import models
from django.contrib.auth.models import User
from tag.models import Tag
from match.rating import jaccard



class Student(models.Model):
    """ Student
    Participates in group collaboration.
    """
    user = models.ForeignKey(User, unique=True)

    def username(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


class Wish(models.Model):
    """
    """
    student = models.ForeignKey(Student)
    tags = models.ManyToManyField(Tag)
    since = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # [!] the distance from a wish object or group object to another
    def distance( self, other, distance_function=jaccard ):
        value = 0.0
        if self != other:
            value = distance_function( self.tags.all(), other.tags.all() )

        return value

    def __unicode__(self):
        return "Wish: " + self.student.__unicode__()


