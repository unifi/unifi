from django.conf.urls import patterns, include, url

urlpatterns = patterns( '',
    url( r'^$', 'group.views.group' ),
)
