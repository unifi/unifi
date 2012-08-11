#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from djangorestframework.resources import ModelResource
from models import Tag

class TagResource(ModelResource):
    model = Tag
    fields = (
        'id',
        'name',
        'score',
        'is_predefined'
    )
    ordering = (
        'name',
        'score',
    )