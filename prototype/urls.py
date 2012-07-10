from django.conf.urls import patterns, include, url
from prototype import views

urlpatterns = patterns( '',

    url( r'tagittest$',               views.tagittest),
    url( r'intrude/([a-z]{1,10})$',   views.intrude ),
    url( r'students/$',               views.display_students ),
    url( r'students/populate/$',      views.populate_students ),
    url( r'wishes/$',                 views.display_wishes ),
    url( r'wishes/populate/$',        views.populate_wishes ),
    url( r'wishes/flush/$',           views.flush_wishes ),
<<<<<<< HEAD
)
=======
    url( r'flush/$',                  views.flush ),
)
>>>>>>> ba747accb301e3138dc7994252b3d16e53359146
