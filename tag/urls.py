#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.conf.urls import patterns, url
from tag.views import *

from djangorestframework.views import \
    ListOrCreateModelView, InstanceModelView, permissions
from resources import TagResource


urlpatterns = patterns('',
    url(
        r'^$',
        ListOrCreateModelView.as_view(
            resource=TagResource,
            permissions=( permissions.IsAuthenticated, )
        )
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        InstanceModelView.as_view(
            resource=TagResource,
            permissions=( permissions.IsAuthenticated, )
        )
    ),
    url(
        r'^distribution/$',
        GetTagDistribution()
    ),
)
