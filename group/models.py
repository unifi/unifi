from django.db import models
from student.models import Student
from oracle.models import Oracle
from tag.models import Tag
from student.models import Wish

class Group(models.Model):
    """
    Group
    Student container.
    """

    wishes           = models.ManyToManyField( Wish )
    students         = models.ManyToManyField( Student, null=True )
    needs_assistance = models.BooleanField()

    def tags(self):
        """
        Return group tags
        """
        return set(
            [ t for w in self.wishes.all() for t in w.tags.all() ]
        )

    def __unicode__(self):
        return "Group " + str(self.pk)
