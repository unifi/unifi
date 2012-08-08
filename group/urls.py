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
        r'^all$', # inspect/all
        views.All()
    ),
    
    url(
        r'^(\d+)',
        views.Inspect()
    ),
    
    url(
        r'^leave/(\d+)$',
        views.Leave()
    ),
)
