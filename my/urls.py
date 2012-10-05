#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.conf.urls import patterns, include, url
from my import views

urlpatterns = patterns( '',

    # A personal front page for each authorized user
    url( r'^$', views.MyView() ),

    # ... allows to create a wish
    url( r'^wish/create', views.CreateWish() ),

    # ... to do a tag-specific search amongst groups
    url( r'^search', views.Search() ),

    # ... It relies on some model-specific views
    url( r'^wish', views.WishView() ),
    url( r'^group', views.GroupView() ),
    url( r'^assistance', views.AssistanceView() ),
)
