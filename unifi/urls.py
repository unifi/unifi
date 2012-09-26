from django.conf.urls import patterns, include, url
from django.contrib import admin
from login.views import Gateway
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns('',

    # admin
    # url(r'^admin/doc/',           include('django.contrib.admindocs.urls')),
    url( r'^admin/',                include(admin.site.urls)),

    # djangorestframework
    url(
        r'^restframework/',
        include( 'djangorestframework.urls',
           namespace='djangorestframework'
        )
    ),

    # root application
    ## main page
    url(
        r'^$',
        Gateway()
    ),

    # inclusive applications
    # url( r'^communication/',       include('communication.urls')),

    url( r'^login/',               include('login.urls')),

    url(
        r'^student/',
        include('student.urls'),
        name="student"
    ),
    url(
        r'^tag/',
        include('tag.urls'),
        name="tag"
    ),

    url(
        r'^match/',
        include('match.urls'),
        name="match"
    ),
    url(
        r'^group/',
        include('group.urls'),
        name="group"
    ),
    url(
        r'^my/',
        include('my.urls'),
        name="my"
    ),
)
