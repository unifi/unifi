from django.conf.urls import patterns, include, url
from socialregistration.views import Setup

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
    url(r'^social/', include('socialregistration.urls',
        namespace='socialregistration')
    ),
    url(r'social/setup/', Setup.as_view() )
)