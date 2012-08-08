from django.db import models
import student.models


# Create your models here.

class Tag(models.Model):
    """
    Describes a topic the student is interested to work on,
    e.g "interface", "linked_list", or subject code, e.g. "inf1010"

    @param  name            the keyphrase or a keyword that constitutes this tag
    @param  score           a cached value that represents tag's popularity
                            just an attempt to oversaturate the model
    @param  predefined      stands for tag's status, if False - the tag
                            was produced by a user, if True - the tag was
                            predefined by the administrator of the bucket
    """
    name = models.CharField( max_length=50, unique=True )
    score = models.DecimalField(
        max_digits=6, decimal_places=5, default="0.0"
    )
    predefined = models.BooleanField( default=False )

    def update_score( self ):
        # [+] draft
        wish = student.models.Wish
        self.score = wish.objects.filter( tags__in=[self] ).count()
        self.save()


    def __unicode__(self):
        return self.name

