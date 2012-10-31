#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from celery import task

from match.pool import WishPool

from timeit import timeit

@task()
def match( distribute_free_wishes=False ):

    def process():
        pool = WishPool()
        pool.create_groups()

    t = timeit( process )

    print "Matching task was executed in {0} seconds".format( t )
