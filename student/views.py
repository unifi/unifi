from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from student.models import Wish
from match.algorithms import *
from core.views import AccessRestrictedView
from unifi.unifi_project_settings import MAX_NUMBER_OF_TAGS
from django.core.exceptions import ObjectDoesNotExist


class DeleteWish( AccessRestrictedView ):
    """
    Removes a wish from the database and the existing matching graph.
    @param pk:    public key of the wish to remove
    """

    def authenticated( self, pk ):
        if self.request.user.is_authenticated:
            student = UserManager.getStudent( self.request.user.username )

            try:
                w = Wish.objects.get(pk=pk)
                WishDispatcher.delete_wish_from_graph(w)
                Wish.objects.get( pk=pk ).delete()
            except ObjectDoesNotExist, ValueError:
                print "-> Client attempted deleting a non-existing record"

        return redirect( "/" )



@csrf_protect
def make_wish(request):

    # [!]
    tag_list =  request.POST.getlist('user[tags][]')

    if len(tag_list) == 0:
        return render_to_response( "dialog.html", {
                "title":    "Error",
                "message":  "lol gife me tags plz"
            },
            context_instance = RequestContext(request)
        )

    #to lower case
    #no shit!?
    tag_list = [t.lower() for t in tag_list]

    if len(tag_list) > MAX_NUMBER_OF_TAGS:
        return render_to_response( "dialog.html", {
                "title":    "Error",
                "message":  "Max num of tags is 5"
            },
            context_instance = RequestContext(request)
        )

    courses = WishDispatcher.extract_course_tag(tag_list)
    if len(courses) > 1:
        return render_to_response( "dialog.html", {
                "title":    "Error",
                "message":  "Please specify one course only"
            },
            context_instance = RequestContext(request)
        )


    usr = UserManager.getStudent(request.user.username)

    #debug
    print request.user.username

    w = WishManager.addWish(usr, tag_list, courses)

    return redirect( "/" )
