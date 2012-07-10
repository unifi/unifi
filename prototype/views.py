from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
# Model imports
from tag.models import Tag
from student.models import Student, Wish

from util import get_project_models





@csrf_protect
def flush( request, target_model = None ):

    """
    Convenience method to flush all model-tables in the database
    except the ones by django and south
    """

    model_names = []
    project_models = []

    if target_model:
        for m in get_project_models():
            if target_model == m.__name__:
                project_models.append( m )
    else:
        project_models = get_project_models()


    for model in project_models:
        model.objects.all().delete()
        model_names.append( model.__name__ )

    return render_to_response( "dialog.html", {
            "title": "Flush entries",
            "message": "Following tables have been flushed: (%s)" \
                % len( model_names ),
            "set": model_names
        },
        context_instance = RequestContext( request )
    )


@csrf_protect
def populate( request ):

    from data.generator import TestDataGenerator

    tdg = TestDataGenerator()

    return redirect( "." )





# Temporary test-specific views
def tagittest (request):
    return render_to_response("add.html", context_instance = RequestContext(request))



@csrf_protect
def intrude( request, username ):

    previous_username = request.user
    auth.logout( request )

    default_password = "123"

    user = auth.authenticate( username=username, password=default_password )

    if user != None:
        auth.login( request, user )

        out = render_to_response( "dialog.html", {
                "title": "Fast intrusion",
                "message": \
                    "You were logged in as: %s, and now you are logged in as %s" \
                    % (previous_username, username),
            },
            context_instance = RequestContext( request )
        )

    else:
        out = render_to_response( "dialog.html", {
                "title": "Fast intrusion failed",
                "message": \
                    "You are still logged in as: %s, user %s was not authenticated" \
                    % (previous_username, username)
            },
            context_instance = RequestContext( request )
        )

    return out


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
