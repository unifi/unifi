
from communication.models import Message
from django.core.mail import send_mail

class EmailEmulating():

    def __init__(self):
        pass

    def toDatabase(self, sender, receiver, message):
        """
            Emulates email sending
        """
        m = Message(sender=sender, receiver=receiver, message=message)
        m.save()

    def toEmail(self, message, sender, receivers):
        """
            Email sending
            @param message: the email message
            @param sender: the sender
            @param receivers: a list with receivers
        """
        print "lolmail"

        sender = sender + '@example.com'
        recv = [r.username() + '@example.com' for r in receivers]

        send_mail('Group found', message, sender,
            recv, fail_silently=False)

