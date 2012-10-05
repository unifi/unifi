#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from celery import task
from celery.task import periodic_task
from datetime import timedelta
from tag.models import Tag
from person.models import Wish

@periodic_task(run_every=timedelta(minutes=30))
def update_score( only_active_wishes=False ):
    """
    Assigns tag-ratings by comparing them to the most popular one.
    @param only_active_wishes:  which wishes to operate on, if false
                                collects tags from all wishes
    """

    wishes       = Wish.objects.filter( is_active=only_active_wishes )
    tags         = Tag.objects.all()
    distribution = {}


    for wish in wishes:
        for tag in wish.tags.all():
            try:
                distribution[tag.name] += 1
            except KeyError:
                distribution[tag.name] = 1

    highest_frequency = float( max( distribution.values() ) )

    for tag in tags:
        try:
            tag.popularity = \
                float( distribution[tag.name] ) / highest_frequency
        except KeyError:
            tag.popularity = 0.0
        tag.save()
