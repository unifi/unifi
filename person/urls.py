#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from person import views
from django.conf.urls import patterns, include, url




urlpatterns = patterns( '',
    url(
        r'^wish/(?P<pk>\d*)$',
        views.SelectWish()
    ),

)


