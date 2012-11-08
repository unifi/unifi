# -*- coding: utf8 -*- 

from unifi.rules import *
from group.models import Group
from celery.task import periodic_task
from communication.emulator import EmailEmulator
from datetime import timedelta


#@periodic_task(run_every=timedelta(minutes=NOTIFICATION_FREQUENCY_MINUTES))
def send_group_notification():
    emulator = EmailEmulator()
    new_groups = Group.objects.filter( is_announced=False )

    for group in new_groups:
        message = emulator.build_message( group )
        for person in group.persons.all():
            emulator.toDatabase( person.user, person.user, message )
        group.is_announced = True
        group.save()


if __name__ == "__main__":
    send_group_notification()