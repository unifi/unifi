import re
from HeapGraphMatcher import *
from match.rating import jaccard
from tag.models import Tag
from student.models import Wish

class WishDispatcher(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(WishDispatcher, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    GROUP_SIZE = 2
    MIN_SCORE = 0.3

    def __init__(self):

        self.bucket_dicts = {}

        #Restoring buckets from database
        for w in Wish.objects.all():
            tags = [t.name_of_tag for t in w.tags.all()]
            courses = self.extract_course_tag(tags)
            if len(courses) >= 1:
                self.add_wish_to_bucket(w, courses[0])
            else:
                print "no course, default bucket"


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
            self.bucket_dicts[tag] = HeapGraphMatcher(2, 0.3, jaccard, tag)

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
        @param: tha wish
        """

        tags = self.extract_course_tag([t.name_of_tag for t in wish.tags.all()])
##        self.bucket_dicts[tags[0]].draw_graph()
        print tags
        print self.bucket_dicts
#        self.bucket_dicts[tags[0]].delete_wish_from_graph(wish)
#        self.bucket_dicts[tags[0]].draw_graph()

