# Create your views here.
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

# Temporary test-specific views
def tagittest (request):
    return render_to_response("tagittest.html", {"title" : "Tagit test", "mesg" : "Register a wish"},
            context_instance = RequestContext(request))

@csrf_protect
def submitwish(request):

    tag_list =  request.POST.getlist('user[tags][]')

    if len(tag_list) == 0:
        return render_to_response("tagittest.html", {"title" : "Tagit test", "mesg" : "lol gife me tags plz"},
                context_instance = RequestContext(request))

    #to lower case
    tag_list = [t.lower() for t in tag_list]

    if len(tag_list) > 5:
        return render_to_response("tagittest.html", {"title" : "Tagit test", "mesg" : "Max num of tags is 5"},
                context_instance = RequestContext(request))

    courses = WishDispatcher.extract_course_tag(tag_list)
    if len(courses) > 1:
        return render_to_response("tagittest.html", {"title" : "Tagit test", "mesg" : "Please specify one course only"},
                context_instance = RequestContext(request))


    usr = UserManager.getStudent(request.user.username)

    #debug
    print request.user.username

    w = WishManager.addWish(usr, tag_list)
    WishDispatcher.add_wish_to_bucket(w, courses[0])

    return render_to_response("submitwish.html", {"title" : "Submit Wish", "wish" : w},
            context_instance = RequestContext(request))

def mywishes(request):

    usr = UserManager.getStudent(request.user.username)
    wishes = WishManager.getAStudentWishes(usr)

    return render_to_response("mywishes.html", {"title" : "My little wishes", "wishes" : wishes },
            context_instance = RequestContext(request))
