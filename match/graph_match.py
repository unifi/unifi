#!/usr/bin/env python2.7

from unifi.management import *
import networkx as nx
import heapq as heap
from itertools import combinations
from rating import jaccard
import pylab
import pickle
import time




#t0 = time.time()
#pairs = combinations(wishes, 2)
#g.add_nodes_from(wishes)

#h = []
#prev = None

#for p in pairs:
#    if p[0] is not prev:
#        for i in range(4):
#            if len(h) == 0:
#                break # my neck
#            hp = heap.heappop(h)

#        h = []
#        prev = p[0]
#    w = 1 - jaccard(p[0].tags.all(), p[1].tags.all())
#    if w < 0.5:
#        g.add_edge(hp[1][0], hp[1][1], weight=hp[0])
#        heap.heappush(h, (w, p))
#

GROUP_SIZE = 3
def check_for_group(wish):
    neighbors = g.adj[wish]
    h = [] # Tha heapzor

    # Add nodes to minheap based on edge-weight (score)
    for n in neighbors.viewitems():
        heap.heappush(h, (n[1], n[0]))


    # A group is found
    if len(h) + 1 >= GROUP_SIZE:
        print "A group is ready!"
        print "Members:",
        print h
        print wish
        print "\n"

wishes = Wish.objects.all()
g = nx.Graph()

for wish in wishes:

    g.add_node(wish)

    # For each existing node, calculate the score between the new wish and the node
    # 0.0 - Perfect match (all tags are the same), 1.0 - No match at all (disjoint tag sets)
    for node in g.nodes():
        if wish.student.user.username == node.student.user.username:
            continue

        score = 1 - jaccard(wish.tags.all(), node.tags.all())

        if score <= 0.3:
            g.add_edge(wish, node, weight=score)

    check_for_group(wish)

#print time.time()-t0

#pos=nx.spring_layout(g, scale=10)
#pylab.figure(10, figsize=(13,12))
#nx.draw(g,pos, font_size=20)
#edge_labels=dict([((u,v,),d['weight']) for u,v,d in g.edges(data=True)])
#nx.draw_networkx_edge_labels(g,pos,edge_labels=edge_labels)
#pylab.show()
#

#g = nx.minimum_spanning_tree(g)

#f = open("graphdump.dat", "wr")
#pickle.dump(g, f)
#f.close()


#subs = nx.connected_component_subgraphs(g)
#pos=nx.spring_layout(g, scale=10)
#pylab.figure(10, figsize=(10,12))

#for s in subs:
#    print sorted(s.adj)
#    nodes = s.nodes()
#    num = len(nodes)
#    if num >= 2: #ant personer
#print nodes


