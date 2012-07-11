# Create your views here.
from group.models import Group
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def allgroups(request):

    g = Group.objects.all()

    return render_to_response("groups.html", {"title": "All available groups",
            "groups": g},
            context_instance = RequestContext(request))
