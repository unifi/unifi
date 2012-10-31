#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from person.models import Wish
from group.models import Group
from networkx import Graph
from networkx.algorithms.clique import find_cliques, cliques_containing_node
from match.rating import jaccard

from match.clique import WishClique as Clique
from match.suggestion import Suggestion


## If the clique-size is low, the likeness demands are high.
## When the clique-size is hight, the likeness demands for clique score are reduced
## When the cliques are found, traverse the unmatched wishes and add them to the
# groups with plausible tagsets

# [+] Skimming: match, skim the unmatched, match the unmatched against the
# the recently created groups

def default_selector( wish ):
    return not wish.is_matched

def default_connector( this, other ):
    return jaccard( this.tags.all(), other.tags.all() )



class WishPool:
    def __init__( self,
                  min_edge_score = 0.50,
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
                        if score >= self.min_edge_weight:
                            self.graph.add_edge( wish, other, weight=score )

        ## processes the graph, excludes lonely nods
        self.connected_nodes = self.update_connected_nodes()
        self.lonely_nodes = self.update_lonely_nodes()
        self.remove_lonely_nodes()
        self.update_cliques()

        ## evaluates alternatives, gathers suggestions for each wish
        # this implies that some cliques occur twice
        self.suggestions = self.update_suggestions()



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

    def update_suggestions( self ):
        suggestions = []
        for wish_pk, cliques in self.get_distributed_cliques().items():
            suggestion = Suggestion(
                Wish.objects.get(pk=wish_pk), cliques )
            suggestions.append( suggestion )
        self.suggestions = suggestions
        return suggestions






if __name__ == "__main__":
    from timeit import timeit
    a = WishPool()

    # creates a list of distinct suggestions
    distinct_cliques = set()

    for s in a.suggestions:
        distinct_cliques.add( s.get_best_clique() )

    for c in distinct_cliques:
        print c.create_group()

    free_wishes = Wish.objects.filter( is_matched=False )
    print free_wishes

