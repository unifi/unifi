#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from celery import task

@task()
def draw_person( person ):
    pass
    # must write to media-location


@task()
def clear_old_wishes():
    pass

