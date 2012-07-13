from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext



def index( request ):



    return render_to_response( "my/gateway.html", {
            "title":    "UNIFI",
            "message":  "Start page"
        },
        context_instance = RequestContext( request )
    )