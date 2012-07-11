from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from student.models import Wish, Student
from tag.models import Tag

from util import *

def match( request ):

    wishes = Wish.objects.all()
    pool = Pool( wishes )
    pairs = sorted( list(pool.pair()), key=lambda x: x[0], reverse=True )

    return render_to_response( "match.html", {
            "title":    "Matching",
            "message":  "Displaying %d pairs" % len(pairs),
            "matches":  pairs
        },
        context_instance = RequestContext( request )
    )
