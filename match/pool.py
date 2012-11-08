#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from person.models import Wish, Person
from group.models import Group
from networkx import Graph
from networkx.algorithms.clique import find_cliques, cliques_containing_node
import networkx as nx
from match.rating import jaccard

from match.clique import WishClique as Clique
from match.suggestion import Suggestion
from match.vitality import group_size_mean, groups_per_wish_mean

from unifi.rules import MIN_NUMBER_OF_EDGES, MIN_EDGE_SCORE


## If the clique-size is low, the likeness demands are high.
## When the clique-size is hight, the likeness demands for clique score are reduced
## When the cliques are found, traverse the unmatched wishes and add them to the
# groups with plausible tagsets

def default_connector( this, other ):
    return jaccard( this.tags.all(), other.tags.all() )



class WishPool:
    def __init__( self,
                  wishes,
                  min_edge_score = MIN_EDGE_SCORE,
                  # min_number_of_edges = MIN_NUMBER_OF_EDGES,
                  connector = default_connector ):
        """
        A filterable pool of wishes represented as nodes. Is used to find
        relations between wishes.

        @param connector: default connector is jaccard
        @return:
        """

        self.graph                 = Graph()
        self.min_edge_weight       = min_edge_score
        # self.min_number_of_edges   = min_number_of_edges

        for wish in wishes:
            self.graph.add_node( wish )
            # loops through the existing nodes in the graph
            for other in self.graph.nodes_iter():
                # compares candidate to all existing nodes except itself
                if other != wish and other.person != wish.person:
                    score = connector( wish, other )
                    if score > self.min_edge_weight:
                        self.graph.add_edge( wish, other, weight=score )

        ## processes the graph, excludes lonely nodes
        self.connected_nodes = self.update_connected_nodes()
        # debug_graph(self.graph, message="Connected nodes are set")
        self.lonely_nodes = self.update_lonely_nodes()
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
        raise NotImplementedError

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

    def create_groups( self ):
        distinct_cliques = set()

        for s in self.suggestions:
            distinct_cliques.add( s.get_best_clique() )

        for c in distinct_cliques:
            c.create_group()

    def get_suggestion_pool( self ):
        return SuggestionPool( self.suggestions )




class SuggestionPool:
    def __init__( self, suggestions ):
        self.suggestions = suggestions

    def exclude_wish( self, wish ):
        for s in self.suggestions:
            s.remove_wish( wish )

    def exclude_clique( self, clique ):
        self.suggestions.remove( clique )

    def get_rated_suggestions( self ):
        # by conflictedness: assumes that the number of the alternative
        # suggestions implies conflictedness
        return sorted( self.suggestions, key=lambda x: len(x), reverse=False )

    def create_groups( self ):
        candidates = set()
        suggestions = self.get_rated_suggestions()

        for s in suggestions:
            candidate = s.get_best_clique()
            if len(candidate) > 1:
                candidates.add( candidate )

        candidates = list( candidates )

        for c in candidates:
            candidates.remove(c)
            c.create_group()
            for w in c.nodes:
                for c in candidates:
                    if w in c.nodes:
                        c.nodes.remove( w )
                    if not len(c) > 1:
                        candidates.remove(c)




def debug_graph( graph, message="" ):
    import matplotlib.pyplot as plt
    print message

    pos = nx.layout.fruchterman_reingold_layout( graph )
    nx.draw( graph, pos )
    nx.draw_graphviz( graph )
    plt.show()


if __name__ == "__main__":
    pass








