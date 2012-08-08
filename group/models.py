from django.db import models
from student.models import Wish, Student

class Group(models.Model):
    """
    Group
    Student container.
    """

    wishes           = models.ManyToManyField( Wish )
    students         = models.ManyToManyField( Student, null=True )
    needs_assistance = models.BooleanField() # [/] rename

    def tags(self):
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
