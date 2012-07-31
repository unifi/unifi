from django.conf.urls import patterns, url
from tag.views import *

urlpatterns = patterns( '',
    url(
        r'^distribution/$',
        GetTagDistribution()
    ),
)
