from django.conf.urls import patterns, include, url
from student import views

urlpatterns = patterns( '',
    url(
        # wish creation from tagger
        r'^wish/make$',
        views.make_wish
    ),
    url(
        # wish removal
        r'^wish/delete/(\d*)$',
        views.DeleteWish()
    ),
)



