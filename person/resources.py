#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from djangorestframework.resources import ModelResource
from django.contrib.auth.models import User
from models import Person, Wish


class UserResource( ModelResource ):
    model = User
    exclude = (
        'password',
    )


class PersonResource( ModelResource ):
    model = Person
    fields = (
        'id',
        ( 'user', UserResource),
        ( 'username', UserResource ),
    )


class WishResource( ModelResource ):
    model = Wish
    fields = (
        (
            'person',
            PersonResource
        ),
        'since',
        'is_active',
        'tags',
    )



