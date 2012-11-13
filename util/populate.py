# -*- coding: utf-8 -*-

import sys

from random import sample, randint

from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from util.generators import StudentGenerator
from util.generators import LetterTagGenerator as TagGenerator
from unifi.management import UserManager, WishManager, TagManager
from person.models import Person, Wish
from tag.models import Tag
from group.models import Group



if __name__ == "__main__":

    Group.objects.all().delete()
    Wish.objects.all().delete()
    Person.objects.exclude( user__username="ilyakh" ).delete()
    User.objects.exclude( username="ilyakh" ).delete()
    Tag.objects.all().delete()

    # set site

    try:
        number_of_persons = int(sys.argv[1])
        number_of_tags = int(sys.argv[2])
        tag_quantity = ( int(raw_input( "min: " )), int(raw_input( "max: " )) )
    except IndexError:
        number_of_persons = 100
        number_of_tags = 2
        tag_quantity = (1, 2)


    UserManager.addPerson( "ilyakh" ).set_password( "123" )
    UserManager.addPerson( "kritisk" ).set_password( "123" )
    UserManager.addPerson( "michael" ).set_password( "123" )
    UserManager.addPerson( "peder" ).set_password( "123" )
    UserManager.addPerson( "rantonse" ).set_password( "123" )
    UserManager.addPerson( "rantonse1" ).set_password( "123" )
    UserManager.addPerson( "rantonse2" ).set_password( "123" )
    UserManager.addPerson( "rantonse3" ).set_password( "123" )

    persons = ( StudentGenerator( 5 ) ).generate( number_of_persons )
    tags = ( TagGenerator() ).generate( number_of_tags )

    print "Creating wishes for {0} persons, with a set of {1} tags".format(
        len(persons), len(tags) )

    for p in persons:
        UserManager.addPerson( p )

    for p in Person.objects.all():

        w = Wish( person=p )
        w.save()

        tq = tag_quantity
        chosen_tags = sample(
            tags, randint( tq[0], tq[1] )
        )

        for t in chosen_tags:
            w.tags.add( TagManager.addTag( t ) )



