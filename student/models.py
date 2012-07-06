from django.db import models
from django.contrib.auth.models import User
from tag.models import Tag

class Student(models.Model):
    """ Student
    Participates in group collaboration.
    """
    user = models.ForeignKey(User, unique=True)

    def username(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


class Wish(models.Model):
    """
    """
    student = models.ForeignKey(Student)
    tags = models.ManyToManyField(Tag)
    wish_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Wish: " + self.student.__unicode__()

