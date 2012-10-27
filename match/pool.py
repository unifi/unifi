#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from person.models import Wish
from group.models import Group
from networkx import Graph
from networkx.algorithms.clique import find_cliques, cliques_containing_node
from match.rating import jaccard


## If the clique-size is low, the likeness demands are high.
## When the clique-size is hight, the likeness demands for clique score are reduced
## When the cliques are found, traverse the unmatched wishes and add them to the
# groups with plausible tagsets

# [+] Skimming: match, skim the unmatched, match the unmatched against the
# the recently created groups

def default_selector( wish ):
    return wish.is_active

def default_connector( this, other ):
    return jaccard( this.tags.all(), other.tags.all() )



class WishPool:
    def __init__( self,
                  min_edge_score = 0.5,
                  # min_number_of_edges = 3,
                  selector = default_selector,
                  connector = jaccard ):
        """
        A filterable pool of wishes represented as nodes. Is used to find
        relations between wishes.

        @param selector: default selector function selects all elements
        @param connector: default connector is jaccard
        @return:
        """

        self.graph                 = Graph()
        self.min_edge_weight       = min_edge_score
        # self.min_number_of_edges   = min_number_of_edges

        for wish in Wish.objects.iterator():
            if selector( wish ):
                self.graph.add_node( wish )
                # loops through the existing nodes in the graph
                for other in self.graph.nodes_iter():
                    # compares candidate to all existing nodes except itself
                    if other != wish and other.person != wish.person:
                        score = connector( wish.tags.all(), other.tags.all() )
                        if score > self.min_edge_weight:
                            self.graph.add_edge( wish, other, weight=score )

        ## processes the graph, excludes lonely nods
        self.connected_nodes = self.update_connected_nodes()
        self.lonely_nodes = self.update_lonely_nodes()
        self.remove_lonely_nodes()
        self.update_cliques()

        ## evaluates alternatives, gathers suggestions
        self.suggestions = []
        for wish_pk, cliques in self.get_distributed_cliques().items():
            suggestion = Suggestion(
                Wish.objects.get(pk=wish_pk), cliques )
            self.suggestions.append( suggestion )

        ## selects appropriate cliques from suggestions
        self.group_candidates = set()
        for s in self.suggestions:
            self.group_candidates.add( s.get_best_clique() )

        ## exposes suggestions, creates groups
        for s in self.group_candidates:
            g = Group()
            g.save()

            for p in s.persons:
                g.persons.add( p )

            for w in s.nodes:
                w.is_active = False # post-processing: deactivates wish
                w.save()
                g.wishes.add( w )
            g.save()


    #def exclude( self, min_number_of_edges=3 ):
    #    for n in self.graph:
    #        if self.graph.number_of_edges( n ) < min_number_of_edges:
    #            self.graph.remove_node( n )
    #    return self.graph

    def update_connected_nodes( self ):
        connected = set()
        for n in self.graph.edges():
            connected.add( n[0] )
        return connected

    def update_lonely_nodes( self ):
        whole_graph = set( self.graph.nodes() )
        return whole_graph.difference( self.connected_nodes )

    def remove_lonely_nodes( self ):
        self.graph.remove_nodes_from( self.lonely_nodes )

    def update_cliques( self ):
        result = set()
        for c in find_cliques( self.graph ):
            if len(c) > 1:
                result.add( Clique(c) )
        self.cliques = result
        return result

    def get_distributed_cliques( self ):
        self.cliques_for_wish = {}
        for n in self.graph.nodes():
            clique_buffer = []
            for c in self.cliques:
                if n in c.nodes:
                    clique_buffer.append( c )
            if len(clique_buffer):
                self.cliques_for_wish[n.pk] = [
                    c for c in clique_buffer if len(c.nodes) > 1 ]
        return self.cliques_for_wish

    def get_conflicting_cliques( self ):
        result = {}
        for w,c in self.get_distributed_cliques():
            if len(c) > 1:
                result[w] = c
        return result

    def rate_cliques( self ):
        result = []
        for c in self.cliques:
            ci = Clique(c)
            result.append( (ci.get_score(), ci) )


class Suggestion:
    def __init__( self, wish, cliques ):
        self.wish = wish        # 1
        self.cliques = cliques  # *

    def get_best_clique( self ):
        if len( self.cliques ) == 1:
            return self.cliques[0]
        else:
            return max( self.get_rated_cliques(), key=lambda t: t[0] )[1]

    def get_rated_cliques( self ):
        result = []

        max_size   =  max( map( lambda c: len( c.nodes ), self.cliques ) )
        max_score  =  max( map( lambda c: c.get_score(), self.cliques ) )

        for c in self.cliques:
            scores = (
                len( c.nodes ) / float( max_size ),
                c.get_score() / float( max_score ),
            )
            mean = sum( scores ) / float( len ( scores ) )
            result.append( ( mean, c ) )

        return sorted( result, key=lambda x: x[0] )


class Clique:
    def __init__( self, nodes ):
        self.nodes = nodes
        self.tags = self.update_tags()
        self.persons = self.update_persons()

    def __len__( self ):
        return len( self.nodes )

    def update_tags( self ):
        result = set()
        for n in self.nodes:
            for t in n.tags.all():
                result.add( t )
        self.tags = result
        return result

    def get_common_tags( self ):
        result = set()
        for n in self.nodes:
            if not len( result ):
                result = set( n.tags.all() )
            else:
                result.intersection_update( n.tags.all() )
        return result

    def get_missing_tags( self ):
        return self.tags.difference( self.get_common_tags() )

    def get_score( self ):
        score = 0.0
        try:
            score = len( self.get_common_tags() ) / float( len( self.tags ) )
        except ZeroDivisionError:
            pass
        return score

    def update_persons( self ):
        result = []
        for n in self.nodes:
            result.append( n.person )
        self.persons = result
        return result


if __name__ == "__main__":
    from timeit import timeit
    a = WishPool()

    free_wishes = Wish.objects.filter( is_active=True )
    print free_wishes

