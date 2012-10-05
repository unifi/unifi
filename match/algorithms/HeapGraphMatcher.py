#!/usr/bin/env python2.7

import networkx as nx
import heapq as heap
from MatchBase import Matcher
from unifi.management import *
from communication.emailemulating import EmailEmulating

class HeapGraphMatcher(Matcher):
    """
    A dynamic group matching algorithm using a priority queue to make groups
    """

    def __init__(self, group_size, min_score, scoring_function, name):
        Matcher.__init__(self, group_size, min_score, scoring_function, name)
        self.mail = EmailEmulating()

    def check_for_group(self, wish):
        neighbors = self.graph.adj[wish]
        h = [] # Tha heapzor

        # Add nodes to minheap based on edge-weight (score)
        # [?] for n in neighbors.viewitems():
        for n in neighbors.items():
            heap.heappush(h, (n[1], n[0]))

        # A group is found (add 1 for the current wish itself)
        if len(h) + 1 >= self.group_size:
            return [ heap.heappop(h) for x in range(self.group_size-1)]

    def add_wish_to_graph(self, wish):
        """
        When a person registers a wish, it is added to the graph
        @param wish: the registered wish
        """

        self.graph.add_node(wish)

        # For each existing node, calculate the score between the new wish and the node
        # 0.0 - Perfect match (all tags are the same), 1.0 - No match at all (disjoint tag sets)
        for node in self.graph.nodes():
            if wish.person == node.person:
                continue

            score = 1 - self.scoring_function(wish.tags.all(), node.tags.all())

            if score <= self.min_score:
                self.graph.add_edge(wish, node, weight=score)

        h = self.check_for_group(wish)

        # A group is found
        # if h is not None:
        #     return self.make_group(wish, h)

    def make_group(self, wish, heap):
        """
        Create a group
        @param wish - the wish that was added (group member)
        @param heap - the list with group members found in the graph
        """

        group = Group()
        group.save()
        group.wishes.add(wish)
        group.persons.add(wish.person)

        for item in heap:
            #Add the wish to the group and remove it from the graph
            group.wishes.add(item[1])
            group.persons.add(item[1].person)
            self.graph.remove_node(item[1])

        # send email to group members
        message = self.mail.build_message(group)
        self.mail.toEmail(message, "Unifi",  group.persons.all())

        # deactivate wish
        wish.is_active = False
        wish.save()
        self.graph.remove_node(wish)
