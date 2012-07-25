import re
from HeapGraphMatcher import *
from match.rating import jaccard
from tag.models import Tag
from student.models import Wish
import networkx as nx

class WishDispatcher(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(WishDispatcher, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def __init__(self, GROUP_SIZE=3, MIN_SCORE=0.6):

        self.bucket_dicts = {}

        self.GROUP_SIZE = GROUP_SIZE 
        self.MIN_SCORE = MIN_SCORE
        self.has_restored = False
        print "The WishDispatcher was initiated"

    def restore_buckets(self):
        """
        Call this method to load wishes from the database and store them in buckets
        """

        print "Restoring" #debug

        if not self.has_restored:
            self.has_restored = True
            for w in Wish.objects.filter(is_active=True):
                tags = [t.name_of_tag for t in w.tags.all()]
                courses = self.extract_course_tag(tags)
                if len(courses) >= 1:
                    self.add_wish_to_bucket(w, courses[0])
                else:
                    self.add_wish_to_bucket(w, "default")

        print "Done restoring" #debug

    def extract_course_tag(self, tags):
        """
        Find the correct bucket/graph to put the wish in
        @param tags: the wish tags
        @return: the name of the bucket
        """

        pattern = r'^[\-\w]+\d{4}'

        return [tag for tag in tags if re.findall(pattern, tag)]

    def add_wish_to_bucket(self, wish, tag):

        #Create new bucket if neccessary
        if not tag in self.bucket_dicts:
            self.bucket_dicts[tag] = HeapGraphMatcher(
                self.GROUP_SIZE, self.MIN_SCORE, jaccard, tag 
            )

        self.bucket_dicts[tag].add_wish_to_graph(wish)


    def get_bucket(self, tag):
        """
        Return the bucket for a given tag
        @param tag: the tag
        @return: the correct bucket
        """

        return self.bucket_dicts[tag]

    def delete_wish_from_graph(self, wish):
        """
        Delete a wish from the graph
        @param: the wish to delete
        """

        try:
            tags = self.extract_course_tag([t.name_of_tag for t in wish.tags.all()])
            if len(tags) == 0:
                self.bucket_dicts["default"].delete_wish_from_graph(wish)
            else:
                self.bucket_dicts[tags[0]].delete_wish_from_graph(wish)
        except:
            print "not in graph"
