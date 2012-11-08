# -*- coding: utf8 -*- 

from person.models import Wish
from group.models import Group

from datetime import timedelta, datetime
from django.utils.timezone import now
from dateutil.parser import parse


def zero_division_safe( func, default=0.0 ):
    def inner():
        try:
            return func()
        except ZeroDivisionError:
            return default
    return inner


@zero_division_safe
def active_wish_mean_age():
    active_wishes = Wish.objects.filter( is_active=True )
    count = active_wishes.count()
    age_seconds = sum( [w.age() for w in active_wishes ] )
    return age_seconds / count


@zero_division_safe
def wish_satisfaction_ratio():
    active = float( Wish.objects.filter( is_active=False ).count() )
    total = float( Wish.objects.count() )
    return active / float( total )



@zero_division_safe
def group_size_mean():
    matched_persons = 0.0
    for g in Group.objects.all():
        matched_persons += g.persons.count()
    group_total = float( Group.objects.count() )
    return matched_persons / float(group_total)


@zero_division_safe
def groups_per_wish_mean():
    group_sum = 0.0
    for w in Wish.objects.all():
        group_sum += w.groups().count()
    wish_total = float( Wish.objects.count() )

    return group_sum / float( wish_total )