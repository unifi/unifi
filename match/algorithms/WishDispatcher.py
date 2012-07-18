import re
from HeapGraphMatcher import *
from match.rating import jaccard

class WishDispatcher(object):

    def __init__(self):
        self.bucket_dicts = {"inf1010" : HeapGraphMatcher(2, 0.3, jaccard, "inf1010"),
            "inf1000" : HeapGraphMatcher(2, 0.3, jaccard, "inf1000")}

    def extract_course_tag(self, tags):
        """
        Find the correct bucket/graph to put the wish in
        @param tags: the wish tags
        @return: the name of the bucket
        """

        pattern = r'^[\-\w]+\d{4}'

        print "mordi"
        return [tag for tag in tags if re.findall(pattern, tag)]

    def add_wish_to_bucket(self, wish, tag):
        self.bucket_dicts[tag].add_wish_to_graph(wish)
