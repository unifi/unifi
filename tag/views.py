# Create your views here.

from core.views import *
from tag.util import TagDistribution
from django.http import HttpResponse



class GetTagDistribution( AccessRestrictedView ):

    def is_authenticated( self ):

        td = TagDistribution()

        return HttpResponse( td.json(), mimetype="application/json" )
