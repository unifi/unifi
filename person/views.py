# -*- coding: utf8 -*-
from django.http import HttpResponse

from match.algorithms import *
from person.models import Wish
from unifi.management import WishManager
from core.views import AccessRestrictedView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect



class SelectWish( AccessRestrictedView ):
    
    def allow( self, pk ):

        response = HttpResponse( status = 200 )

        try:
            wish = Wish.objects.get( pk=pk )

            if self.request.method == "GET":
                response = self.dialog(
                    title = "Displaying wish number %s" % pk,
                    message = "%s" % wish,
                    collection = wish.tags.all()
                )

            elif self.request.method == "DELETE":

                if wish.person.user == self.user:
                    # the user owns the object
                    wish.is_active = False
                    wish.save()
                else:
                    # the user does not own the object
                    response = HttpResponse( status = 403 )

        except ObjectDoesNotExist, ValueError:
            # the corresponding object with a given pk is not found
            response = HttpResponse( status = 404 )

        return response