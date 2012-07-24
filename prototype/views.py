from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from os import listdir, mkdir
from tag.models import Tag
from student.models import Student, Wish
from unifi.management import *
from util import get_project_models, get_project_models_dict



PROFILES_PATH = "/".join( [".", __package__, "data", "profiles"] )

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

    project_models.append( User )

    for model in project_models:
        model.objects.all().delete()
        model_names.append( model.__name__ )


    return render_to_response( "dialog.html", {
            "title": "Flush entries",
            "message": "Following tables have been flushed: (%s)" \
                % len( model_names ),
            "set": model_names
        },
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


    return render_to_response( "dialog.html", {
            "title": "The database is now populated",
            "message": "By profile %s" % profile,
            "set": ""
        },
        context_instance = RequestContext( request )
    )

def generate( request, profile=None ):

    MIN_TAG_QUANTITY = 1
    MAX_TAG_QUANTITY = 5
    SINGLE_WISH_PER_USER = False
    WISH_TAG_SEPARATOR = " "

    all = []

    def to_int( parameter, default=0 ):
        try:
            return int( parameter )
        except TypeError:
            return default

    if profile:

        # make a profile-folder if none is found
        profile_location = "/".join([ PROFILES_PATH, profile ])
        try:
            mkdir( profile_location )
        except OSError:
            pass # the profile was not present and had to be created


        from generators import \
            StudentGenerator, \
            WordTagGenerator, \
            WishGenerator

        quantity, location, options = {}, {}, {}
        options['wish'] = {}


        quantity['student']     = to_int( request.GET.get('Student') )
        quantity['tag']         = to_int( request.GET.get('Tag') )
        quantity['wish']        = to_int( request.GET.get('Wish') )

        options['wish']['min_tag_quantity'] = \
            to_int( request.GET.get('min_tag_quantity'), 1 )
        options['wish']['max_tag_quantity'] = \
            to_int( request.GET.get('max_tag_quantity'), 5 )

        location['student']     = "/".join( [profile_location, "Student"] )
        location['tag']         = "/".join( [profile_location, "Tag"])
        location['wish']        = "/".join( [profile_location, "Wish"] )

        students, tags, wishes = [], [], []

        print options["wish"]["min_tag_quantity"], options["wish"]["max_tag_quantity"]

        if quantity['student'] > 0:
            students = ( StudentGenerator() ).generate( quantity['student'] )
            with open( location['student'], "w" ) as output:
                output.write( "\n".join(students) )

        else:
            students = open( location['student'], "r" ).readlines()
            students = [s.strip() for s in students]

        if quantity['tag'] > 0:
            tags = ( WordTagGenerator() ).generate( quantity['tag'] )
            with open( location['tag'], "w" ) as output:
                output.write( "\n".join(tags) )
        else:
            tags = open( location['tag'], "r" ) \
                .readlines()
            tags = [t.strip() for t in tags]

        # these models depend on other objects in the database
        # their count can be defined, but cannot
        wishes = []

        print quantity['wish'], len(tags), len(students)

        if quantity['wish'] > 0 and len(tags) > 0 and len(students) > 0:
            wishes = ( WishGenerator( students, tags ) ).generate(
                quantity['wish'],
                options['wish']['min_tag_quantity'],
                options['wish']['max_tag_quantity'],
                SINGLE_WISH_PER_USER
            )
            with open( location['wish'], "w" ) as output:
                buffer = []
                for w in wishes:
                    buffer.append(
                        "%s %s" % ( w[0], WISH_TAG_SEPARATOR.join( w[1] ) )
                    )
                output.write( "\n".join(buffer) )

        all = \
            [ "Student: " + s for s in students ] + \
            [ "Tag: " + s for s in tags ] + \
            [ s for s in wishes ]

    return render_to_response( "dialog.html", {
            "title": "Generated objects",
            "message": "",
            "set": all
        },
        context_instance = RequestContext( request )
    )


def intrude_fork( request ):

    students = Student.objects.all()

    return render_to_response( "prototype/intrudefork.html", {
            "title": "Intrude as a Student",
            "students": sorted( students, key=lambda x: x.username() )
        },
        context_instance = RequestContext( request )
    )



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


def leave( request ):
    auth.logout( request )
    return redirect( "/" )

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


def graph( request ):
    
    edges = []
    data = {
        'students':     Student.objects.count(),
        'tags':         Tag.objects.count(),
        'wishes':       Wish.objects.count(),
        'groups':       Group.objects.count(),
    }

    for group in Group.objects.all():
        students = group.students.all()

        for student in students:
            if students[0].pk != student.pk:
                edges.append(
                    ( group.pk, students[0], student )
                )

    return render_to_response( "prototype/graph.html", {
            "edges": edges,
            "data": data,
        }
    )