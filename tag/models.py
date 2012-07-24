from django.db import models

# Create your models here.

class Tag(models.Model):
    """
    A tag describes something a student is interested to work with, e.g "interface",
    "linked_list", or subject code, e.g "inf1010"
    """
    name_of_tag = models.CharField( max_length=50, unique=True )

    def __unicode__(self):
        return self.name_of_tag
