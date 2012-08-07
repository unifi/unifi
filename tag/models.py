from django.db import models

# Create your models here.

class Tag(models.Model):
    """
    Describes a topic the student is interested to work on,
    e.g "interface", "linked_list", or subject code, e.g. "inf1010"

    @param
    """
    name = models.CharField( max_length=50, unique=True )
    predefined = models.BooleanField( default=False )

    def __unicode__(self):
        return self.name
