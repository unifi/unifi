# -*- coding: utf8 -*-

from django.test import TestCase
from actor.models import *
from django.contrib.auth.models import User


class SimpleTest(TestCase):

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)



if __name__ == "__main__":

    r = Role.objects.get_or_create( name="Student" )[0]
    r.save()
    u = User.objects.get_or_create( username="ilyakh" )[0]
    u.save()
    p = Person.objects.get_or_create( user=u )[0]
    p.save()
    s = Slot( person=p, role=r, is_leader=True )
    s.save()
    g = Group()
    g.save()


    s1 = Slot( person=None, role=r )
    s2 = Slot( person=None, role=r )
    s3 = Slot( person=None, role=r )
    s4 = Slot( person=None, role=r )

    map( lambda x: x.save(), [s1, s2, s3, s4] )

    g.slots.add( s1, s2, s3, s4 )

    g = Group.objects.all()[3]

    print g.slots.all().get(role=Role.by_name("Student")).person.user.username
    print g.members.all()

