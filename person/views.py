# -*- coding: utf8 -*-
from django.http import HttpResponse
from person.models import Wish
from core.views import AccessRestrictedView, MethodView


class SelectWish( AccessRestrictedView ):
    def allow( self, pk ):
        response = HttpResponse( status = 200 )
        try:
            wish = Wish.objects.get( pk=pk )
            if self.request.method == "GET":
                if self.person.is_owner_of( wish ):
                    response = self.dialog(
                        title = "Displaying wish number %s" % pk,
                        message = "%s" % wish,
                        collection = wish.tags.all()
                    )
                else:
                    response = HttpResponse( status=403 )
            elif self.request.method == "DELETE":
                if self.person.is_owner_of( wish ):
                    wish.is_active = False
                    wish.save()
                else:
                    response = HttpResponse( status = 403 )

        except Wish.DoesNotExist, ValueError:
            response = HttpResponse( status = 404 )

        return response
