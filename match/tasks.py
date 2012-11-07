#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from unifi.rules import ALGORITHM_VERSION

from celery import task
from celery.task import periodic_task
from timeit import timeit
from datetime import timedelta
from json import dumps, loads

from match.pool import WishPool
from person.models import Wish, Person
from match.vitality import *
from match.models import Report

@task()
def match( distribute_free_wishes=False ):

    report = {
        'cycles':                   -1,
        'elapsed_time':             0.0,
        'satisfaction_ratio':       0.0,
    }

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
        report['cycles'] += 1
        report['elapsed_time'] += timeit( process, number=1 )


    report['satisfaction_ratio'] = wish_satisfaction_ratio()
    report['active_wishes'] = Wish.objects.count_active()
    report['groups_per_wish_mean'] = groups_per_wish_mean()
    report['group_size_mean'] = group_size_mean()

    return report



@task()
def skim():
    free_wishes = Wish.objects.filter( is_active=True )
    for w in free_wishes:
        pass


@periodic_task(run_every=timedelta(minutes=2))
def match_only():
    report = match()
    json_report = dumps(report)
    report_archive = Report( data=json_report, version=ALGORITHM_VERSION )
    report_archive.save()


if __name__ == "__main__":
    report = match()

    from json import dumps

    # save report to the database
    json_report = dumps(report)
    report_archive = Report( data=json_report, version=ALGORITHM_VERSION )
    report_archive.save()

    print json_report
