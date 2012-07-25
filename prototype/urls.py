from django.conf.urls import patterns, include, url
from prototype import views
from util import get_project_models

urlpatterns = patterns( '',
    
    url(
        r'^intrude/([a-z]{1,10})$',
        views.intrude
    ),

    # allows developer to choose which user to login as
    url(
        r'^intrude/$',
        views.intrude_fork
    ),

    # logout
    url(
        r'^leave/',
        views.leave
    ),

    # views
    url(
        r'^graph/$',
        views.graph
    ),

    url(
        r'^students/$',
        views.display_students
    ),

    url(
        r'^wishes/$',
        views.display_wishes 
    ),
    
    url(
        r'^tags/$',
        views.display_tags
    ),    

    url( 
        r'^flush/$',
        views.flush 
    ),

    # allows flushing of a specific model supplied after the forward-slash
    url(
        r'^flush/('+"|".join([ m.__name__ for m in get_project_models()])+')$',
        views.flush
    ),

    # populates the database by a given test-data profile
    url(
        r'^populate/(\w{1,32})$',
        views.populate
    ),

    # generates a profile with a set of given specifications
    url(
        r'^generate/(\w{1,32})$',
        views.generate
    ),

    # generates wishes based on a set of Tags and Users

)
