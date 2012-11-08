# -*- coding: utf8 -*- 

from django.conf.urls import patterns, include, url
from communication.views import All

urlpatterns = patterns('',
    url(
        r'^',
        All()
    ),
)