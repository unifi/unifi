# -*- coding: utf8 -*- 

from django.contrib.sites.models import Site

try:
    s = Site.objects.get( pk=1 )
    s.domain = "127.0.0.1:8000"
    s.save()
except Exception:
    print "Failed"
    pass
