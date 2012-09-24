
from unifi.management import *

from HeapGraphMatcher import *
from MatchBase import Matcher
from match.rating import jaccard
#from WishDispatcher import WishDispatcher

class A():

    def __init__(self):
        self.myvar = 2
        pass

    def __call__(self, tag):
        print "extract tags"
        print "and add wish to graph"
        print self.myvar

