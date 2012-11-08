# -*- coding: utf8 -*- 

from core.views import AccessRestrictedView
from communication.models import Message

class All( AccessRestrictedView ):
    def allow( self ):
        messages = Message.objects.all()
        return self.dialog( title="Correspondence", collection=messages )