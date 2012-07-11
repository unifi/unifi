from django.conf.urls import patterns, include, url
from student import views

urlpatterns = patterns( '',
     url( r'tagittest$',               views.tagittest),
     url(r'submitwish$',    views.submitwish),
)

