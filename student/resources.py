#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from djangorestframework.resources import ModelResource
from django.contrib.auth.models import User
from models import Student, Wish


class UserResource( ModelResource ):
    model = User
    exclude = (
        'password',
    )


class StudentResource( ModelResource ):
    model = Student
    fields = (
        'id',
        ( 'user', UserResource),
        ( 'username', UserResource ),
    )


class WishResource( ModelResource ):
    model = Wish
    fields = (
        (
            'student',
            StudentResource
        ),
        'since',
        'is_active',
        'tags',
    )



