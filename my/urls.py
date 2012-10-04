#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.conf.urls import patterns, include, url
from my import views

urlpatterns = patterns( '',

    # a personal front page belonging to each user's account
    url( r'^$', views.MyView() ),

    # search
    url( r'^search/', views.Search() ),

    # model-specific views
    url( r'^wish/', views.WishView() ),
    url( r'^group/', views.GroupView() ),
    url( r'^assistance/', views.AssistanceView() ),

)
