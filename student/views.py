# -*- coding: utf8 -*-
from django.http import HttpResponse

from match.algorithms import *
from student.models import Wish
from unifi.management import WishManager
from core.views import AccessRestrictedView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, redirect
from unifi.unifi_project_settings import MAX_NUMBER_OF_TAGS





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

                if wish.student.user == self.user:
                    # the user owns the object
                    WishManager.deleteWish( wish )
                else:
                    # the user does not own the object
                    response = HttpResponse( status = 403 )

        except ObjectDoesNotExist, ValueError:
            # the corresponding object with a given pk is not found
            response = HttpResponse( status = 404 );

        return response



class CreateWish( AccessRestrictedView ):

    def allow( self, *args, **kwargs ):
        # default to a redirect back to the page
        # [/] use self.error method
        result = redirect( "/" )

        tag_list =  self.request.POST.getlist('user[tags][]')
        tag_list = [ t.lower() for t in tag_list ]

        if not len( tag_list ):
            result =  self.dialog( "Error", "No tags given" )

        elif len( tag_list ) > MAX_NUMBER_OF_TAGS:
            result = self.dialog( "Error",
                "Your wish contains too many tags. Specify max %d tags." % \
                MAX_NUMBER_OF_TAGS
            )

        courses = WishDispatcher.extract_course_tag( tag_list )

        if len( courses ) > 1:
            result = self.dialog( "Error", "Please specify a course" )


        user = UserManager.getStudent( self.request.user.username )
        WishManager.addWish(
            user,
            tag_list,
            courses
        )

        return result