from django.conf.urls import patterns, include, url
from prototype import views
from util import get_project_models

urlpatterns = patterns( '',

    url( r'tagittest$',               views.tagittest),
    url( r'intrude/([a-z]{1,10})$',   views.intrude ),
    url( r'students/$',               views.display_students ),
    url( r'students/populate/$',      views.populate_students ),
    url( r'wishes/$',                 views.display_wishes ),
    url( r'wishes/populate/$',        views.populate_wishes ),
    url( r'wishes/flush/$',           views.flush_wishes ),

    url(
        r'intrude/([a-z]{1,10})$',
        views.intrude
    ),

    url(
        r'students/$',
        views.display_students
    ),

    url(
        r'wishes/$',
        views.display_wishes ),

    url( r'flush/$',                  views.flush ),

    # allows flushing of a specific model supplied after the forward-slash
    url(
        r'flush/('+"|".join([ m.__name__ for m in get_project_models()])+')$',
        views.flush
    ),

    url(
        r'populate/$',
        views.populate
    ),
)
