#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.conf.urls import patterns, url
from djangorestframework import permissions
from djangorestframework.views import \
    ListOrCreateModelView, InstanceModelView
from group import views
from group.resources import GroupResource



urlpatterns = patterns( '',

    url(
        r'^$',
        ListOrCreateModelView.as_view(
            resource=GroupResource,
            permissions=( permissions.IsAuthenticated, )
        )
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        InstanceModelView.as_view(
            resource=GroupResource,
            permissions=( permissions.IsAuthenticated, )
        )
    ),



    # old
#    url(
#        r'^(?P<pk>\d*)$',
#        views.Select()
#    ),
#
#    url(
#        r'^(?P<group_pk>\d*)/member/(?P<member_pk>\d*)$',
#        views.SelectMember()
#    ),
#
    url(
        r'^all$', # inspect/all
        views.All()
    ),
#
#    url(
#        r'^(\d+)',
#        views.Inspect()
#    ),



)

