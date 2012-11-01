#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from django.conf.urls import patterns, url
from tag.views import *



urlpatterns = patterns('',
    url(
        r'^distribution/$',
        GetTagDistribution()
    ),
)
