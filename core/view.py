#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from django.views.generic.base import TemplateView

class AccessRestrictedView( TemplateView ):
    def __call__(self, request, *args, **kwargs ):



if __name__ == "__main__":
    pass