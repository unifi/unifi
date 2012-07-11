from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from os import listdir, mkdir
from tag.models import Tag
from student.models import Student, Wish
from unifi.management import *
from util import get_project_models, get_project_models_dict



PROFILES_PATH = "/".join( [".", __package__, "data", "profiles"] )

@csrf_protect
def flush( request, target_model=None ):

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
def populate( request, profile=None ):

    if profile:
                
        if profile in listdir( PROFILES_PATH ):
            
            # gets the current directory
            file_location = "/".join([ PROFILES_PATH, profile ])
            # removes the extension
            file_names = [ f.split(".")[0] for f in listdir(file_location) ]

            data = {}

            # collects objects for each file
            for f in file_names:
                target = "/".join( [file_location, f] )
                with open( target, "r" ) as source:
                    data[f] = [ line.strip() for line in source.readlines() ]

            if "Tag" in data.keys():
                for tag in data["Tag"]:
                    TagManager.addTag( tag )

            if "Student" in data.keys():
                for student in data["Student"]:
                    UserManager.addStudent( student )

            if "Wish" in data.keys():
                separator = " "
                for wish in data["Wish"]:
                    wish = wish.split( separator )
                    WishManager.addWish( wish[0], wish[1:] )


    return redirect( "." )


@csrf_protect
def generate( request, profile=None ):

    MIN_TAG_QUANTITY = 1
    MAX_TAG_QUANTITY = 5
    WISH_SEPARATOR = " "

    if profile:
        profile_location = "/".join([ PROFILES_PATH, profile ])
        try:
            mkdir( profile_location )
        except OSError:
            pass


        wish_quantity, tag_quantity, student_quantity = 0, 0, 0

        from generator import TestDataGenerator
        generator = TestDataGenerator()

        try:
            student_quantity = int( request.GET.get( 'student' ) )

            if student_quantity > 0:
                students = generator.generate_students( student_quantity )
                with open( "/".join([ profile_location, "Student" ]), "w" ) as output:
                    output.write( "\n".join( students ) )
            else:
                students = open(
                    "/".join([ profile_location, "Student" ]), "r"
                ).readlines()
        except TypeError:
            pass

        try:
            tag_quantity = int( request.GET.get( 'tag' ) )
            if tag_quantity > 0:
                tags = generator.generate_tags( tag_quantity )
                with open( "/".join([ profile_location, "Tag" ]), "w" ) as output:
                    output.write( "\n".join( tags ) )
            else:
                tags = open(
                    "/".join([ profile_location, "Tag" ]), "r"
                ).readlines()
        except TypeError:
            pass

        try:
            wish_quantity = int( request.GET.get( 'wish' ) )
            if wish_quantity > 0:
                wishes = generator.generate_wishes(
                    students,
                    tags,
                    wish_quantity,
                    min_tag_quantity=MIN_TAG_QUANTITY,
                    max_tag_quantity=MAX_TAG_QUANTITY
                )
                wishes = [ "%s %s" % ( w[0], WISH_SEPARATOR.join( w[1] )) for w in wishes ]
                with open( "/".join([ profile_location, "Wish" ]), "w" ) as output:
                    output.write( "\n".join( wishes ) )
        except TypeError:
            pass
        except UnboundLocalError:
            wishes = open(
                "/".join([ profile_location, "Wish" ]), "w"
            ).readlines()
            with open( "/".join([ profile_location, "Wish" ]), "r" ) as output:
                output.write( "\n".join( wishes ) )


    return redirect( "." )

@csrf_protect
def intrude( request, username ):

    previous_username = request.user
    auth.logout( request )

    default_password = "123"

    user = auth.authenticate( 
        username=username, 
        password=default_password 
    )

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
    
    return render_to_response( "dialog.html", {
            "title": "All registered students",
            "message": "Listing %d students" % ( Student.objects.count() ),
            "set": Student.objects.all()
        },
        context_instance = RequestContext( request )
    )

def display_tags( request ):
    tags = Tag.objects.all()
    output = []

    return render_to_response( "dialog.html", {
            "title": "All registered tags",
            "message": "Listing %d tags" % ( Tag.objects.count() ),
            "set": Tag.objects.all()
        },
        context_instance = RequestContext( request )
    ) 
    
def display_wishes( request ):
    wishes = Wish.objects.all()

    output = []
    for w in wishes:
        output.append(
            ( w.student.username, w.tags.all() )
        )

    return render_to_response( "wishlist.html", {
            "title": "Wish register",
            "message": "Following wishes were captured in the database",
            "wishlist": output
        },
        context_instance = RequestContext( request )
    )
