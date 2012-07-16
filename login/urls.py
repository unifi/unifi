from django.conf.urls import patterns, include, url
from django.contrib import admin

from login import views

urlpatterns = patterns('',
    url(
        r'^gateway/',
        views.gateway
    ),
)