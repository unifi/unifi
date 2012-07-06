from django.db import models

# Create your models here.

class Tag(models.Model):
    """ Tag
    A keyword that describes a certain expertise,
    either possessed by an Oracle or required by a Student.
    """
    name_of_tag = models.CharField( max_length=50, unique=True )

    def __unicode__(self):
        return self.name_of_tag