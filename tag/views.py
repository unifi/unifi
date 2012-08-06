from django.shortcuts import render_to_response
from django.template.context import RequestContext
from core.views import AccessRestrictedView
from tag.util import TagDistribution
from django.http import HttpResponse



class GetTagDistribution( AccessRestrictedView ):

    """
    Returns a quantative distribution of tags throughout the database.
    @param  format      calls a function that conforms the response to
                        a specified 'format' (json, html)

    """

    def allow( self ):

        td = TagDistribution()
        response_format = self.request.GET.get('format')

        if response_format == "json":
            return self.json( td )
        else:
            return self.html( td )



    def json( self, tag_distribution ):
        return HttpResponse(
            tag_distribution.json(), mimetype="application/json"
        )

    def html( self, tag_distribution ):
        return render_to_response( "dialog.html", {
                "title":    "Tags in the Database",
                "message":  "",
                "set":      tag_distribution().items()
            },
            context_instance = RequestContext( self.request )
        )
