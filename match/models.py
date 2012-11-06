# -*- coding: utf8 -*-

from django.db import models

# The composite values that that base on the values in the same table
# can be either saved explicitly (surrendering the ability to
# calculate them with new formulas and new data gathering approaches.
# Or to be calculated dynamically in model class' functions.


#class Report( models.Model ):
#    date = models.DateField( auto_created=True )
#    number_of_groups = models.IntegerField( default=0 )
#    number_of_matched_wishes = models.IntegerField( default=0 )
#    number_of_free_wishes = models.IntegerField( default=0 )
#    group_size_mean = models.FloatField( default=0.0 )
#    groups_per_wish_mean = models.FloatField( default=0.0 )
