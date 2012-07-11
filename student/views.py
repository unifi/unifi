# Create your views here.
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from student.models import Wish, Student

from unifi.management import *

# Temporary test-specific views
def tagittest (request):
    return render_to_response("tagittest.html", {"mesg" : "Register a wish"},
            context_instance = RequestContext(request))

@csrf_protect
def submitwish(request):

    tag_list =  request.POST.getlist('user[tags][]')

    #to lower case
    tag_list = [t.lower() for t in tag_list]

    if len(filter(lambda tag: tag.startswith(("inf", "mat", "fys")), tag_list)) > 1:
        return render_to_response("tagittest.html", {"mesg" : "Please specify one course only"}, context_instance =
            RequestContext(request))


    usr = UserManager.getStudent(request.user.username)

    #For testing
    w = WishManager.addWish(usr, tag_list)

    return render_to_response("submitwish.html", {"wish" : w},
            context_instance = RequestContext(request))
