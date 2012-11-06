# -*- coding: utf8 -*-

from django.db import models

class Report( models.Model ):
    created = models.DateField( auto_now_add=True )
    version = models.CharField( max_length=32, null=True )
    data = models.TextField()

