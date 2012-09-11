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

        # normalizes the score
        if len( self.tag_dict.values() ):
            max_tag_score = max( self.tag_dict.values() )
        else: # if the tagset is empty
            max_tag_score = 0.0

        for k,v in self.tag_dict.items():
            key = k.name

            output.append( {
                'value': key,
                'label': key,
                'score': (float(v) / self.num_tags_wishes_distinct) /\
                         (float(max_tag_score) / self.num_tags_wishes_distinct)
            } )

        # sorts the dictionary in score descending order
        output = sorted( output, key=lambda e: e["score"], reverse=True )

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
        Run through the wishes and gather statistics.
        Must be rewritten to account for the heavy load
        against the server backend.
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

        #Total number of distinct tags in the database.
        for t in Tag.objects.all():
            self.num_tags_db_total += 1
