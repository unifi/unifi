#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from celery import task
from tag.models import Tag
from person.models import Wish

@task()
def update_score():
    for t in Tag.objects.all():
        w.

        t.score = 0.0
        t.save()
