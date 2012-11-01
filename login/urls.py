# -*- coding: utf8 -*-

from django.conf.urls import patterns, include, url

from login.views import UnifiSetup

from login import views

urlpatterns = patterns('',
    url(
        r'^enter/$',
        views.Login()
    ),
    url(
        r'^gateway/$',
        views.Gateway()
    ),
    url(
        r'^leave/$',
        views.Leave()
    ),
    url(
        r'social/setup/',
        UnifiSetup.as_view()
    ),
    url(
        r'^social/',
        include('socialregistration.urls', namespace='socialregistration')
    ),
)
