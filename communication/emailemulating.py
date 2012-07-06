
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

    def toEmail(self, message, sender, receiver, *receivers):
        """
            Email sending
        """

        sender = sender.username + '@example.com'

        recv = [r.username + '@example.com' for r in receivers]
        recv.append(receiver.username + '@example.com')

        send_mail('Subject Here', message, sender,
            recv, fail_silently=False)

