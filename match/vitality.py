# -*- coding: utf8 -*- 

from person.models import Wish
from group.models import Group


def wish_satisfaction_ratio():
    free = float( Wish.objects.filter( is_active=False ).count() )
    total = float( Wish.objects.count() )

    return free / float( total )


def group_size_mean():
    # wishes per group mean
    matched_persons = 0.0
    for g in Group.objects.all():
        matched_persons += g.persons.count()
    group_total = float( Group.objects.count() )

    return matched_persons / float(group_total)


def groups_per_wish_mean():
    group_sum = 0.0
    for w in Wish.objects.all():
        group_sum += w.groups().count()
    wish_total = float( Wish.objects.count() )

    return group_sum / float( wish_total )