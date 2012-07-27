from student.models import Wish
from unifi.management import TagManager
from tag.models import Tag

class TagDistribution():
    """
    Tag statistics
    """

    def __init__(self):
        self.tag_dict = {}
        self.num_tags_db_total = 0
        self.num_tags_wishes_distinct = 0
        self.num_tags_wishes_total = 0

        self.gather_statistics()

    def __getitem__(self, tag_name):

        if tag_name.__class__ == str:
            tag_name = TagManager.getTag(tag_name)

        return self.tag_dict[tag_name]


    def wipe(self):
        """
        Safety
        """
        self.tag_dict = {}
        self.num_tags_db_total = 0
        self.num_tags_wishes_distinct = 0
        self.num_tags_wishes_total = 0

    def gather_statistics(self):
        """
        Run through the wishes and gather statistics
        """
        distinct_set = set()
        self.wipe()

        for wish in Wish.objects.all():
            for tag in wish.tags.all():
                self.num_tags_wishes_total += 1
                distinct_set.add(tag)
                if not tag in self.tag_dict:
                    self.tag_dict[tag] = 1
                else:
                    self.tag_dict[tag] += 1

        self.num_tags_wishes_distinct = len(distinct_set)

        #Total number of distinct tags in database.
        for t in Tag.objects.all():
            self.num_tags_db_total += 1
