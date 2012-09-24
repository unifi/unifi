from django.conf.urls import patterns, include, url
from match import views

urlpatterns = patterns( '',
    url(
        r'^$',
        views.Match()
    ),
)