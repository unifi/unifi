from django.conf.urls import patterns, include, url

urlpatterns = patterns( '',
    url( r'all$', 'group.views.all' ),
)
