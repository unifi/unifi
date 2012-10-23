# -*- coding: utf-8 -*-

import sys

from random import sample, randint

from util.generators import StudentGenerator, LetterTagGenerator
from unifi.management import UserManager, WishManager, TagManager
from person.models import Person, Wish
from tag.models import Tag


if __name__ == "__main__":

    Wish.objects.all().delete()
    Person.objects.all().delete()
    Tag.objects.all().delete()

    try:
        number_of_persons = sys.argv[1]
        number_of_tags = sys.argv[2]
        tag_quantity = ( raw_input( "max: " ), raw_input( "min: " ) )
    except IndexError:
        number_of_persons = 50
        number_of_tags = 10
        tag_quantity = (3, 5)


    persons = ( StudentGenerator( 5 ) ).generate( number_of_persons )
    tags = ( LetterTagGenerator() ).generate( number_of_tags )

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
