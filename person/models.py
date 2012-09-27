#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.db import models
from django.contrib.auth.models import User
from tag.models import Tag



class Person(models.Model):
    """ Person
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
    person = models.ForeignKey(Person)
    tags = models.ManyToManyField(Tag)
    since = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return "Wish: " + self.person.__unicode__()


