# -*- coding: utf8 -*-

from communication.models import Message
from django.core.mail import send_mail

class EmailEmulator:
    def toDatabase(self, sender, receiver, message):
        """
        Emulates email sending. "Emails" are just stored as a database record
        @param sender: the sender
        @type sender: User object
        @param receiver: the receiver
        @type receiver: User object
        @param message: the message
        """

        m = Message( sender=sender, receiver=receiver, message=message )
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

    def build_message( self, group ):
        person_list = ",".join( [ p.user.username for p in group.persons.all() ] )
        message = (
            "Dette brevet er sendt fra UNIFI, den automatiske kollokviegeneratoren",
            "",
            "Nå er du en medlem av Gruppe#{0}!".format( group.pk ),
            "",
            "Som består av deg og {0}".format( person_list ),
            "",
            "Til felles har dere følgende interesser {0}".format( group.common_tags ),
            "",
        )


        return message
