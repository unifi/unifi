#!/usr/bin/env python2.7

from unifi.management import *
import networkx as nx
import heapq as heap
from itertools import combinations
from rating import jaccard
import pylab
import time

GROUP_SIZE = 10
MIN_SCORE = 0.8

def check_for_group(wish):
    neighbors = g.adj[wish]
    h = [] # Tha heapzor

    # Add nodes to minheap based on edge-weight (score)
    for n in neighbors.viewitems():
        heap.heappush(h, (n[1], n[0]))


    # A group is found (add 1 for the current wish itself)
    if len(h) + 1 >= GROUP_SIZE:
        return [ heap.heappop(h) for x in range(GROUP_SIZE-1)]

wishes = Wish.objects.all()
g = nx.Graph()
t0 = time.time()

for wish in wishes:

    g.add_node(wish)

    # For each existing node, calculate the score between the new wish and the node
    # 0.0 - Perfect match (all tags are the same), 1.0 - No match at all (disjoint tag sets)
    for node in g.nodes():
        if wish.student == node.student:
            continue

        score = 1 - jaccard(wish.tags.all(), node.tags.all())

        if score <= MIN_SCORE:
            g.add_edge(wish, node, weight=score)

    h = check_for_group(wish)

    if h is not None:
        print "A group is found \n(%d) Members: " % (len(h)+1),
        print wish, 
        print ":", 

        for item in h:
            print item[1],
            g.remove_node(item[1])

        g.remove_node(wish)

        print "\n"

print "Time: " + str(time.time()-t0) + " s"

pos=nx.spring_layout(g, scale=10)
pylab.figure(10, figsize=(13,12))
nx.draw(g,pos, font_size=20)
edge_labels=dict([((u,v,),d['weight']) for u,v,d in g.edges(data=True)])
nx.draw_networkx_edge_labels(g,pos,edge_labels=edge_labels)
pylab.show()
