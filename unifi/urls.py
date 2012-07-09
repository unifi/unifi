from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # admin
    url( r'^admin/',                include(admin.site.urls)),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # root application
    url( r'^$',                     'unifi.views.main' ),
    url( r'^add/$',                 'unifi.views.add' ),
    url( r'^display/$',             'unifi.views.display' ),
    url( r'^flush/$',               'unifi.views.flush' ),
    # other project applications
    # url( r'^communication/',       include('communication.urls')),
    # url( r'^crap/',                include('match.urls')),
    url( r'^group/',                include('group.urls')),
    # url( r'^login/',               include('login.urls')),
    url( r'^match/',                 include('match.urls')),
    # url( r'^oracle/',              include('oracle.urls')),
    # url( r'^prototype/',           include('prototype.urls')),
    # url( r'^student/',             include('student.urls')),
    # url( r'^tag/',                 include('tag.urls')),
    # url( r'^unifi/',               include('unifi.urls')),
    # url( r'^util/',                include('util.urls')),
)
