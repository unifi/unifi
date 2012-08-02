from django.conf.urls import patterns, url
from group import views

urlpatterns = patterns( '',
    url(
        r'^all$', # inspect/all
        views.All()
    ),
    
    url(
        r'^(\d+)',
        views.Inspect()
    ),
    
    url(
        r'^leave/(\d+)$',
        views.Leave()
    ),
)
