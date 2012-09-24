#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from djangorestframework.resources import ModelResource
from django.contrib.auth.models import User
from models import Group
from student.resources import StudentResource, UserResource, WishResource
from tag.resources import TagResource

class GroupResource( ModelResource ):
    model = Group

    fields = (
        ( 'students', StudentResource ),
        ( 'wishes', WishResource ),
        ( 'tags', TagResource ),
        'needs_assistance',
    )