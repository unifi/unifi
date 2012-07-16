
from unifi.management import *

from HeapGraphMatcher import *
from MatchBase import Matcher
from match.rating import jaccard

graph = HeapGraphMatcher(3, 0.4, jaccard)

wishes = Wish.objects.all()

for wish in wishes:
    graph.add_wish_to_graph(wish)

graph.draw_graph()
