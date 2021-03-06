#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.conf.urls import patterns, url
from group import views



urlpatterns = patterns( '',

    url(
        r'^(?P<pk>\d*)$',
        views.Select()
    ),

    url(
        r'^(?P<group_pk>\d*)/member/(?P<member_pk>\d*)$',
        views.SelectMember()
    ),

    url(
        r'^all$',
        views.All()
    ),

    url(
        r'^assistance$',
        views.Assistance(),
        name="assistance"
    ),

    url(
        r'^(?P<pk>\d*)/correspondence$',
        views.Contact()
    ),
)
