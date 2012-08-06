
from communication.models import Message
from django.core.mail import send_mail

class EmailEmulating():

    def __init__(self):
        pass

    def toDatabase(self, sender, receiver, message):
        """
        Emulates email sending. "Emails" are just stored as a database record
        @param sender: the sender
        @type sender: User object
        @param receiver: the receiver
        @type receiver: User object
        @param message: the message
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

        sender += '@example.com'
        recv = [r.username() + '@example.com' for r in receivers]

        send_mail('Group found', message, sender,
            recv, fail_silently=False)

    def build_message(self, group):
        """
        Build an email-message
        @param group: the group that is created
        """

        message = "A group for has been found!\n" \
                + "Group tags: " + ", ".join(group.tags().values_list("name_of_tag", flat=True)) \
                + "\nGroup members: " + ", ".join(group.students.all().values_list("user__username", flat=True)) \
                + "\nTa kontakt med dine gruppmedlemmer og avtal tid og sted."

        return message
