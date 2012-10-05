#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from celery import task
from match.util import *
from match.rating import jaccard


# debug
from time import time
#

@task()
def match_groups():
    pool = Pool()
    for name, bucket in pool.buckets.items():
        # creates groups in each bucket
        strategy = Strategy( bucket, jaccard )
        strategy.create_groups()
