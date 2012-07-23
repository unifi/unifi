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
    is_active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return "Wish: " + self.student.__unicode__()


# class Proposal( models.Model ):
    # """
    # A group membership suggestion sent to a user by the system.
    
    # The user chooses either to accept or to withdraw from a Proposal.
    # The withdrawal results in return of his associated Wish back into 
    # the graph.
    
    # This operation is equal to the Wish-reactivation from the earlier
    # version.
    
    # Possible extensions:
    # * Can be garbage-collected by a specific timeout based upon tag popularity.
    # * Can be coupled with the communication framework
    # """
    
    # students = models.ManyToManyField( Student )
    # wishes = models.ManyToManyField( Wish )
    
    # def tags( self ):
        # """
        # @return     a set of all tags in all wishes of a given proposal
        # """
        # return set(
            # [   
                # tag 
                # for wish in self.wishes.all() 
                # for tag in wish.tags.all() 
            # ]
        # )