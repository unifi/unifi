# -*- coding: utf8 -*- 

from person.models import Wish
from group.models import Group

for w in Wish.objects.all():
    w.is_active = True
    w.save()

Group.objects.all().delete()
