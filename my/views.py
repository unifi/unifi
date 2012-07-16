from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext

from group.models import Group
from student.models import *
from unifi.management import UserManager



def index( request ):

    """
    Presents an authenticated user's state in the system: the related objects.
    """

    user = request.user
    candidates = Student.objects.filter( user=user )

    if len(candidates) == 0:
        student = None
    else:
        student = candidates[0]


    if request.user.is_authenticated():

        wishes = Wish.objects.filter( student=student )
        groups = Group.objects.filter( students__in=[student] )

        return render_to_response( "my/gateway.html", {
                "title":    "UNIFI",
                "greeting":  "Velkommen tilbake, %s!" % student.username(),
                "groups":   groups,
                "wishes":   wishes
            },
            context_instance = RequestContext( request )
        )

    else:

        return redirect( "/" )