# -*- coding: utf8 -*- 

from django.db import models

class WishManager( models.Manager ):
    def count_active( self ):
        return self.get_query_set().filter( is_active=True ).count()