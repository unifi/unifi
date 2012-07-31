#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from student.models import Wish
from unifi.management import TagManager
from tag.models import Tag
from django.http import HttpResponse

import json

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


    def __call__(self):
        return self.tag_dict

    def json( self ):
        output = []
        max_tag_score = max( self.tag_dict.values() )
        for k,v in self.tag_dict.items():
            key = k.name_of_tag
            output.append( {
                'value': key,
                'label': key,
                'score': (float(v) / self.num_tags_wishes_distinct) /\
                         (float(max_tag_score) / self.num_tags_wishes_distinct)
            } )

        return json.dumps( output, sort_keys=True, indent=4 )


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
