#!/usr/bin/env python2.7

urlpatterns = patterns( '',
    url( r'^students/$',               'views.display_students' ),
    url( r'^students/populate/$',      'views.populate_students' ),
    url( r'^wishes/$',                 'views.display_wishes' ),
    url( r'^wishes/populate/$',        'views.populate_wishes' ),
    url( r'^wishes/flush/$',           'views.flush_wishes' ),
    url( r'^intrude/([a-z]{1,10})',    'views.intrude' ),
)