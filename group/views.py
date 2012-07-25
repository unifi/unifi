from django.shortcuts import render_to_response
from django.template.context import RequestContext
from group.models import Group

def all(request):
    groups = Group.objects.all()

    return render_to_response( "group/all.html", {
            "standalone": True,
            "title": "All groups",
            "groups": groups,
        },
        context_instance = RequestContext(request)
    )
