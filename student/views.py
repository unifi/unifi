# Create your views here.
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from student.models import Wish, Student
from tag.models import Tag

import match

from controls import *

# Temporary test-specific views
def tagittest (request):
    return render_to_response("add.html", context_instance = RequestContext(request))


