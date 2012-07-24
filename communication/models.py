from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    """
    Emulate e-mail messages
    """

    sender = models.ForeignKey(User, related_name='msg_sender') 
    receiver = models.ForeignKey(User, related_name='msg_receiver')
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Between " + self.sender.__unicode__() + ", " \
            + self.receiver.__unicode__() + ": " + self.message

