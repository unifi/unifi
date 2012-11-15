#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from unifi.rules import *

from celery.task import periodic_task
from timeit import timeit
from datetime import timedelta
from json import dumps, loads

from match.pool import WishPool
from person.models import Wish, Person
from match.vitality import *
from match.models import Report



def match():

    report = {}

    if Wish.objects.active().count() < MIN_NUMBER_OF_ACTIVE_WISHES:
        print "Match process skipped"
        return None

    report = {
        'cycles':                   -1,
        'elapsed_time':             0.0,
        'satisfaction_ratio':       0.0,
    }

    def process():
        pool = WishPool( Wish.objects.filter( is_active=True ) )
        sp = pool.get_suggestion_pool()
        sp.create_groups()

        free_wishes = Wish.objects.filter( is_active=True )
        event_message = "\n".join([
                "Active wishes: {0}".format( free_wishes.count() ),
                "{0}".format( free_wishes ),
                "Groups/Wish (mean): {0}".format( groups_per_wish_mean() ),
                "Group size (mean): {0}".format( group_size_mean() )

        ])
        print event_message
        print

    last_remainder = Wish.objects.active().count() +1
    while last_remainder > Wish.objects.active().count() and last_remainder > 0:
        last_remainder = Wish.objects.active().count()
        report['cycles'] += 1
        report['elapsed_time'] += timeit( process, number=1 )


    report['satisfaction_ratio']    = wish_satisfaction_ratio()
    report['active_wishes']         = Wish.objects.active().count()
    report['groups_per_wish_mean']  = groups_per_wish_mean()
    report['group_size_mean']       = group_size_mean()
    report['active_wish_mean_age']  = active_wish_mean_age()

    return report



def skim():
    free_wishes = Wish.objects.filter( is_active=True )
    for w in free_wishes:
        pass


@periodic_task(run_every=timedelta(minutes=PROCESS_FREQUENCY_MINUTES))
def match_only():
    report = match()

    if report:
        json_report = dumps(report)
        report_archive = Report( data=json_report, version=ALGORITHM_VERSION )
        report_archive.save()


if __name__ == "__main__":
    match_only()