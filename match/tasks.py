#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from celery import task
from timeit import timeit
from match.pool import WishPool
from person.models import Wish, Person
from match.vitality import *

@task()
def match( distribute_free_wishes=False ):
    def process():
        pool = WishPool()
        sp = pool.get_suggestion_pool()
        sp.create_groups()

        free_wishes = Wish.objects.filter( is_active=True )
        print "Free wishes: ", len(free_wishes), free_wishes

        try:
            print "Mean groups per Wish: {0}".format(
                groups_per_wish_mean() )
            print "Mean group size: {0}".format(
                group_size_mean() )
        except ZeroDivisionError:
            pass

    last_remainder = Wish.objects.count_active() +1
    while last_remainder > Wish.objects.count_active() and last_remainder > 0:
        last_remainder = Wish.objects.count_active()
        print "Matching task was executed in {0} seconds".format(
            timeit( process, number=1 ) )



@task
def skim():
    free_wishes = Wish.objects.filter( is_active=True )
    for w in free_wishes:
        pass

if __name__ == "__main__":
    match()
