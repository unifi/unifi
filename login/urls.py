from django.conf.urls import patterns, include, url
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
        r'^register/$',
        views.Register()
    ),
)