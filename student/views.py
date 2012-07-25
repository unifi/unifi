# Create your views here.#No course - "default" bucket
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from student.models import Wish, Student
from match.algorithms import *
from unifi.management import *
from unifi.unifi_project_settings import MAX_NUMBER_OF_TAGS

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
