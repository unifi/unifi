from django.conf.urls import patterns, include, url
from tag.views import *

urlpatterns = patterns( '',
    url(
        r'^distribution/$',
        GetTagDistribution()
    ),
)
