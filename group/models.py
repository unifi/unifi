# -*- coding: utf8 -*-

from django.db import models
from person.models import Wish, Person

class Group(models.Model):
    """
    Group. A person container.
    """

    wishes           = models.ManyToManyField( Wish )
    persons         = models.ManyToManyField( Person, null=True )
    needs_assistance = models.BooleanField()


    def tags( self ):
        """
        Return group tags as a models.query.QuerySet
        """

        wishes = self.wishes.all()
        tags = wishes[0].tags.all()
        for w in wishes[1:]:
            tags = tags | w.tags.all()

        return tags.distinct()

    def __unicode__(self):
        return "Group " + str(self.pk)
