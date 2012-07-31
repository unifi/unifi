from django.conf.urls import patterns, include, url
from my import views

urlpatterns = patterns( '',

    # a personal front page belonging to each user's account
    url( r'^$', views.MyView() ),

    # a list of wishes of the user
    # allows user to:
    # - manage wishes: edit and remove the existing wishes
    # - list wishes: allows user to list his current wishlist
    # - accept a match: lets user to accept a match and enter a group
    #       match -> group process
    # - link to add wishes: allows user to procede to wish
    # url( r'^wishes/$', views.wishes ),

    # a list of groups the user is in
    # url( r'^groups/$', views.groups ),


)
