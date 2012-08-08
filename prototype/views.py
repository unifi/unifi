# -*- coding: utf8 -*-

from core.views import AccessRestrictedView, DevelopmentOnlyView
from prototype.generators import RealNameStudentGenerator
from util import get_project_models, get_project_models_dict
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from student.models import Student, Wish
from django.contrib import auth
from unifi.management import *
from tag.models import Tag
from os import listdir, mkdir


PROFILES_PATH = "/".join( [".", __package__, "data", "profiles"] )
WISH_TAG_SEPARATOR = "\t"
TAG_SEPARATOR = ","


class Leave( DevelopmentOnlyView ):

    def allow( self ):
        """
        A silent logout routine
        """
        auth.logout( self.request )
        return redirect( "/" )

class Flush( DevelopmentOnlyView ):

    def allow( self, target_model=None ):
        model_names = []
        project_models = []

        if target_model:
            for m in get_project_models():
                if target_model == m.__name__:
                    project_models.append( m )
        else:
            project_models = get_project_models()

        if target_model is None:
            project_models.append( User )

        for model in project_models:
            model.objects.all().delete()
            model_names.append( model.__name__ )

        
        return self.dialog( 
            title       =  "Flush entries",
            message     =  "Following tables have been flushed: (%s)" % len( model_names ),
            collection  =  model_names
        );


class Populate( DevelopmentOnlyView ):

    def allow( self, profile=None ):

        if profile:
            if profile in listdir( PROFILES_PATH ):
                data = {}
                # gets the current directory
                file_location = "/".join([ PROFILES_PATH, profile ])
                # removes the extension
                file_names = [ f.split(".")[0] for f in listdir(file_location) ]

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
                    # the separator between 'wish.student'(1) and 'wish.tags'(*)
                    separator = "\t"
                    for wish in data["Wish"]:
                        wish = wish.split( separator )
                        WishManager.addWish(
                            wish[0], wish[1].split( TAG_SEPARATOR )
                        )

        return render_to_response( "dialog.html", {
                "title": "The database is now populated",
                "message": "By profile %s" % profile,
                "set": ""
            },
            context_instance = RequestContext( self.request )
        )

class Generate( DevelopmentOnlyView ):

    def allow( self, profile=None ):
        """
        This view is acts as an interface to generators package.
        """

        MIN_TAG_QUANTITY = 1
        MAX_TAG_QUANTITY = 5
        SINGLE_WISH_PER_USER = False

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


            quantity['student']     = to_int( self.request.GET.get('Student') )
            quantity['tag']         = to_int( self.request.GET.get('Tag') )
            quantity['wish']        = to_int( self.request.GET.get('Wish') )

            options['wish']['min_tag_quantity'] = \
                to_int( self.request.GET.get('min_tag_quantity'), 1 )
            options['wish']['max_tag_quantity'] = \
                to_int( self.request.GET.get('max_tag_quantity'), 5 )

            location['student']     = "/".join( [profile_location, "Student"] )
            location['tag']         = "/".join( [profile_location, "Tag"])
            location['wish']        = "/".join( [profile_location, "Wish"] )

            students, tags, wishes = [], [], []

            print options["wish"]["min_tag_quantity"], options["wish"]["max_tag_quantity"]

            if quantity['student'] > 0:
                students = ( RealNameStudentGenerator() ).generate( quantity['student'] )
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
                            "%s%s%s" % ( w[0], WISH_TAG_SEPARATOR, TAG_SEPARATOR.join( w[1] ) )
                        )
                    output.write( "\n".join(buffer) )

            all = \
                [ "Student: " + s for s in students ] + \
                [ "Tag: " + s for s in tags ] + \
                [ s for s in wishes ]




        if self.request.GET.get('populate'):
            return redirect( "/prototype/populate/%s" % profile )
        else:
            return self.dialog(
                "Generated objects",
                collection = all
            )


class Intrude( DevelopmentOnlyView ):

    def allow( self, username ):
        """
        Allows a developer switch the associated user records quickly.
        This gives any user public access to any account and must therefore
        be disabled in production mode.

        @param username:  the username of the user to log in as

        """

        previous_username = self.user
        auth.logout( self.request )

        default_password = "123"

        user = auth.authenticate(
            username=username,
            password=default_password
        )

        if user is not None:
            auth.login( self.request, user )

            response = redirect( "/" )

        else:
            response = self.dialog( "Fast intrusion failed",
                "You are still logged in as: %s, user %s was not authenticated" % \
                    (previous_username, username)
            )

        return response

class VisualIntrude( DevelopmentOnlyView ):

    def allow( self ):
        students = Student.objects.all()
        oracles = [o.user.username for o in Oracle.objects.all() ]

        return render_to_response( "prototype/intrude.html", {
                "title": "Intrude as a Student",
                "students": sorted( students, key=lambda x: x.username() ),
                "oracles": oracles
            },
            context_instance = RequestContext( self.request )
        )


class Graph( DevelopmentOnlyView ):

    def allow( self ):
        """
        Composes a relation graph for each group. The edges are set up from
        the first user to each user of the group.
        """

        def mean_group_size():
            group_count = 0
            student_count = 0
            for g in Group.objects.all():
                group_count += 1
                student_count += g.students.count()
            try:
                return float(student_count) / group_count
            except ZeroDivisionError:
                return -999999999



        edges = []
        groups = []
        data = {
            'students':             Student.objects.count(),
            'tags':                 Tag.objects.count(),
            'wishes':               Wish.objects.count(),
            'groups':               Group.objects.count(),
            'mean_group_size':      mean_group_size()
        }

        for group in Group.objects.all():
            groups.append( group )
            students = group.students.all()

            for student in students:
                if students[0].pk != student.pk:
                    edges.append(
                        ( group.pk, students[0], student )
                    )

        return render_to_response( "prototype/graph.html", {
                "edges": edges,
                "groups": groups,
                "data": data,
            },
            context_instance = RequestContext( self.request )
        )



class ListStudents( DevelopmentOnlyView ):
    def allow( self ):
        return render_to_response( "dialog.html", {
                "title": "All registered students",
                "message": "Listing %d students" % ( Student.objects.count() ),
                "set": Student.objects.all()
            },
            context_instance = RequestContext( self.request )
        )

class ListTags( DevelopmentOnlyView ):

    def allow( self ):
        return render_to_response( "dialog.html", {
                "title": "All registered tags",
                "message": "Listing %d tags" % ( Tag.objects.count() ),
                "set": Tag.objects.all()
            },
            context_instance = RequestContext( self.request )
        )

class ListWishes( DevelopmentOnlyView ):
    def allow( self ):

        detailed_wishes = [
                ( w.student, w.tags.all() ) for w in Wish.objects.all()
            ]

        return render_to_response( "dialog.html", {
                "title": "Wish register",
                "message": "Following wishes were captured in the database",
                "set": detailed_wishes
            },
            context_instance = RequestContext( self.request )
        )