from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from student.models import Wish
from match.algorithms import *
from core.views import AccessRestrictedView
from django.core.exceptions import ObjectDoesNotExist
from unifi.unifi_project_settings import MAX_NUMBER_OF_TAGS


class DeleteWish( AccessRestrictedView ):
    """
    Removes a wish from the database and the existing matching graph.
    @param pk:    public key of the wish to remove
    """

    def allow( self, pk ):
        if self.request.user.is_authenticated:
            student = UserManager.getStudent( self.request.user.username )

            try:
                w = Wish.objects.get(pk=pk)
                WishDispatcher.delete_wish_from_graph(w)
                Wish.objects.get( pk=pk ).delete()
            except ObjectDoesNotExist, ValueError:
                print "-> Client attempted deleting a non-existing record"

        return redirect( "/" )


class SelectWish( AccessRestrictedView ):
    
    def allow( self, pk ):
        
        wish = Wish.objects.get( pk=pk )
        
        return self.dialog( 
            title = "Displaying wish number %s" % pk,
            message = "%s" % wish,
            collection = wish.tags.all()
        )
        

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
                "Your wish contains too many tags"
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

        
