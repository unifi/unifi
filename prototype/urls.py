from django.conf.urls import patterns, include, url
from prototype import views
from util import get_project_models

urlpatterns = patterns( '',
    
    url(
        r'^intrude/([a-z]{1,10})$',
        views.Intrude()
    ),

    # allows developer to choose which user to login as
    url(
        r'^intrude/$',
        views.VisualIntrude()
    ),

    # logout
    url(
        r'^leave/',
        views.Leave()
    ),

    # views
    url(
        r'^graph/$',
        views.Graph()
    ),

    url( 
        r'^flush/$',
        views.Flush()
    ),

    # allows flushing of a specific model supplied after the forward-slash
    url(
        r'^flush/('+"|".join([ m.__name__ for m in get_project_models()])+')$',
        views.Flush()
    ),

    # populates the database by a given test-data profile
    url(
        r'^populate/(\w{1,32})$',
        views.Populate()
    ),

    # generates a profile for a set of given specifications
    url(
        r'^generate/(\w{1,32})$',
        views.Generate()
    ),

    url(
        r'^students/$',
        views.ListStudents()
    ),

    url(
        r'^wishes/$',
        views.ListWishes()
    ),

    url(
        r'^tags/$',
        views.ListTags()
    ),
)
