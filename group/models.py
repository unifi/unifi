from django.db import models
from student.models import Student
from oracle.models import Oracle
from tag.models import Tag



class Group(models.Model):
    """ Group
    Student container.
    Requires assistance from an Oracle.
    """
    tags     = models.ManyToManyField( Tag )
    students = models.ManyToManyField( Student, null=True )
    oracle   = models.OneToOneField( Oracle, null=True ) # !

    def __unicode__(self):
        return "Group" #TODO change this
