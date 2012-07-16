#!/usr/bin/env python2.7

import networkx as nx
import heapq as heap
from MatchBase import Matcher

class HeapGraphMatcher(Matcher):
    """
    A group matching algorithm using a priority queue to make groups
    """

    def __init__(self, group_size, min_score, scoring_function):
        Matcher.__init__(self, group_size, min_score, scoring_function)

    def check_for_group(self, wish):
        neighbors = self.graph.adj[wish]
        h = [] # Tha heapzor

        # Add nodes to minheap based on edge-weight (score)
        for n in neighbors.viewitems():
            heap.heappush(h, (n[1], n[0]))

        # A group is found (add 1 for the current wish itself)
        if len(h) + 1 >= self.group_size:
            return [ heap.heappop(h) for x in range(self.group_size-1)]


    def add_wish_to_graph(self, wish):
        """
        When a student registers a wish, it is added to the graph
        @param wish: the registered wish
        """

        self.graph.add_node(wish)

        # For each existing node, calculate the score between the new wish and the node
        # 0.0 - Perfect match (all tags are the same), 1.0 - No match at all (disjoint tag sets)
        for node in self.graph.nodes():
            if wish.student == node.student:
                continue

            score = 1 - self.scoring_function(wish.tags.all(), node.tags.all())

            if score <= self.min_score:
                self.graph.add_edge(wish, node, weight=score)

        h = self.check_for_group(wish)

        if h is not None:
            print "A group is found \n(%d) Members: " % (len(h)+1),
            print wish, 
            print ":", 

            for item in h:
                print item[1],
                self.graph.remove_node(item[1])

            self.graph.remove_node(wish)

            print "\n"

