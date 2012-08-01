from django.conf.urls import patterns, url
from group import views

urlpatterns = patterns( '',
    url(
        r'^all$',
        views.All()
    ),
)
