# -*- coding: utf8 -*-

class Suggestion:
    def __init__( self, wish, cliques ):
        self.wish = wish        # 1
        self.cliques = cliques  # *

    def __len__( self ):
        return len( self.cliques )

    def is_conflicted( self ):
        return len(self.cliques) > 1

    def remove_wish( self, wish ):
        for c in self.cliques:
            if wish in c.nodes:
                c.nodes.remove( wish )

    def get_best_clique( self ):
        if len( self.cliques ) == 1:
            return self.cliques[0]
        else:
            return max( self.get_rated_cliques(), key=lambda t: t[0] )[1]

    def get_rated_cliques( self ):
        result = []

        max_size   =  max( map( lambda c: len( c.nodes ), self.cliques ) )
        max_score  =  max( map( lambda c: c.get_score(), self.cliques ) )

        scores = {}
        for c in self.cliques:
            if len(c.nodes) > 1:
                scores['size'] = len( c.nodes ) / float( max_size )
                scores['relative'] = c.get_score() / float( max_score )
            else:
                scores['size'] = 0.0

            mean = sum( scores.values() ) / float( len ( scores.values() ) )
            result.append( ( mean, c ) )

        return sorted( result, key=lambda x: x[0] )


    # [-] remove
    def get_rating( self ):

        # Alternatives: 1. score mean 2. conflictedness

        rated_cliques = self.get_rated_cliques()
        scores = [s[0] for s in rated_cliques]
        result = 0.0
        try:
            result = sum(scores) / float(len(scores))
        except ZeroDivisionError:
            pass



        return result
