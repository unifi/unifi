# -*- coding: utf8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from core.views import AccessRestrictedView
from unifi.management import UserManager
from group.models import Group
from student.models import *


from django import template

register = template.Library()


class VerbatimNode(template.Node):

    def __init__(self, text):
        self.text = text

    def render(self, context):
        return self.text


@register.tag
def verbatim(parser, token):
    text = []
    while 1:
        token = parser.tokens.pop(0)
        if token.contents == 'endverbatim':
            break
        if token.token_type == template.TOKEN_VAR:
            text.append('{{')
        elif token.token_type == template.TOKEN_BLOCK:
            text.append('{%')
        text.append(token.contents)
        if token.token_type == template.TOKEN_VAR:
            text.append('}}')
        elif token.token_type == template.TOKEN_BLOCK:
            text.append('%}')
    return VerbatimNode(''.join(text))

class MyView( AccessRestrictedView ):

#    def allow( self ):
#
#        candidates = Student.objects.filter(
#            user=self.request.user
#        )
#
#        if len(candidates):
#            student = candidates[0]
#        else:
#            student = None
#
#
#        if self.request.user.is_authenticated():
#
#            # assistance_groups = sample( list( Group.objects.all() ), 10 )
#
#            # for g in assistance_groups:
#                # g.needs_assistance = True
#                # g.save()
#
#            assistance_groups = Group.objects.filter( needs_assistance=True )
#
#            wishes = Wish.objects.filter( student=student )
#            wishes = [ w for w in wishes if w.is_active ]
#
#            groups = Group.objects.filter( students__in=[student] )
#
#            autocomplete = Tag.objects.all()
#
#            # for u in sample( list(Student.objects.all()), 10 ):
#                # UserManager.updateUser( u.username(), "o" )
#
#            return render_to_response( "my/index.html", {
#                    "title":                "UNIFI",
#                    "groups":               groups,
#                    "wishes":               wishes,
#                    "assistance_groups":    assistance_groups,
#                },
#                context_instance = RequestContext( self.request )
#            )
#
#        else:
#            return redirect( "/" )


    def allow( self ):

                return render_to_response( "my/handlebars.html", {
                        "title":                "UNIFI",
                    },
                    context_instance = RequestContext( self.request )
                )


