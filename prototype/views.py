from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from student.models import Wish


# Temporary test-specific views
def tagittest (request):
    return render_to_response("add.html", context_instance = RequestContext(request))



@csrf_protect
def intrude( request, username ):

    previous_username = request.user
    auth.logout( request )
    user = auth.authenticate( username=username, password="123" )

    if user != None:
        auth.login( request, user )

        out = render_to_response( "dialog.html", {
            "title": "Fast intrusion",
            "message": "You were logged in as: %s, and now you are logged in as %s" % (previous_username, username),
            },
            context_instance = RequestContext( request )
        )

    else:
        out = render_to_response( "dialog.html", {
            "title": "Fast intrusion failed",
            "message": "You are still logged in as: %s, user %s was not authenticated" % (previous_username, username)
        },
            context_instance = RequestContext( request )
        )

    return out;


@csrf_protect
def flush( request ):

    tables = [Tag, Student, Wish]

    map( lambda x: x.objects.all().delete(), tables )
    table_names = ", ".join([ table.__name__ for table in tables ])

    return render_to_response( "dialog.html", {
        "title": "Flush entries",
        "message": "The tables for %s has been flushed" % ( table_names )
    },
        context_instance = RequestContext( request )
    )


def display_students( request ):
    users = Student.objects.all()
    output = [u.username for u in users]

    return render_to_response( "dialog.html", {
        "title": "All registered students",
        "message": "Listing %d students" % (len(output)),
        "set": output
    },
        context_instance = RequestContext( request )
    )


def populate_students( request ):
    data = open( "./gen/test/users.dat", "r" ).readlines();

    from management.usermanagement import UserManagement
    manager = UserManagement()

    for line in data:
        manager.addUser( line )
        manager.updateUser( line, arg="s" )

    return redirect( "/test/students/" )


def populate_wishes( request ):
    SEPARATOR = " "
    data = open( "./gen/test/wishes.dat", "r" ).readlines();

    from management.wishmanagement import WishManagement
    manager = WishManagement()

    for line in data:
        candidate = line.split( SEPARATOR )
        manager.addWish( candidate[0], candidate[1:] )

    return redirect( "/test/wishes/" )

def display_wishes( request ):
    wishes = Wish.objects.all()

    output = []
    for w in wishes:
        output.append(
            (w.student.username, w.tags.all())
        )

    return render_to_response( "wishlist.html", {
        "title": "Wish register",
        "message": "Following wishes were captured in the database",
        "wishlist": output
    },
        context_instance = RequestContext( request )
    )

def flush_wishes( request ):
    Wish.objects.all().delete()

    return render_to_response( "dialog.html", {
        "title": "All wishes were deleted",
        "message": "All wishes were removed from the databased.",
        },
        context_instance = RequestContext( request )
    )
