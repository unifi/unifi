from django.conf.urls import patterns, include, url
from student import views

urlpatterns = patterns( '',
    url(
        # wish creation from tagger
        r'^wish/(?P<pk>\d+)$',
        views.SelectWish()
    ),
    url(
        # wish creation from tagger
        r'^wish/create$',
        views.CreateWish()
    ),
    url(
        # wish removal
        r'^wish/delete/(\d*)$',
        views.DeleteWish()
    ),
)



