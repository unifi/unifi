import pylab
import networkx as nx
import time

class Matcher:
    """
    A base class that matching algorithms can derive.
    Supports basic operations
    """

    def __init__(self, group_size, min_score, scoring_function):
        """
            @param group_size: the number of students on a group
            @param min_score: the minimum score for two wishes to be considered "good match"
            @param scoring_function: the function used to score match between wishes
        """
        self.group_size = group_size
        self.min_score = min_score
        self.scoring_function = scoring_function
        self.graph = nx.Graph()


    def make_group(self):
        pass

    def draw_graph(self):
        """
        Draw a "nice" visualization of a graph with matplotlib
        """

        pos=nx.spring_layout(self.graph, scale=10)
        pylab.figure(10, figsize=(13,12))
        nx.draw(self.graph,pos, font_size=20)
        edge_labels=dict([((u,v,),d['weight']) for u,v,d in self.graph.edges(data=True)])
        nx.draw_networkx_edge_labels(self.graph,pos,edge_labels=edge_labels)
        pylab.show()

    def gettime(self):
        return time.time()