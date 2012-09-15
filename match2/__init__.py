#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

import re
from student.models import Wish
from tag.models import Tag
from match.rating import jaccard

import networkx as network


def is_bucket( tag ):
    pattern = r'^\w{3}\d{4}$'
    return re.match( pattern, tag )

def get_unique_active_tags():
    from student.models import Wish

    unique_active_tags = set()
    for wish in Wish.objects.all():
        for tag in wish.tags.all():
            unique_active_tags.add( tag )

    return unique_active_tags

def get_wishes_tagged_by( tag ):
    from student.models import Wish
    return Wish.objects.filter( tags__in=[tag] )

def distribute_wishes_by_tag():
    distribution = {}
    for wish in Wish.objects.all():
        for tag in Wish.tags.all():
            if distribution[tag.name]:
                distribution[tag.name].append(wish)
            else:
                distribution[tag.name] = [wish]
    return distribution

def distribute_wishes_by_tags( self ):
    for wish in Wish.objects.all():
        for tag in wish.tags.all():
            if not self.buckets.get(tag.name):
                self.buckets[tag.name] = Bucket( tag )
            self.buckets[tag.name].add( wish )
    return self.buckets





class Pool:
    def __init__( self ):
        self.buckets = dict()
        # creates the default bucket
        self.buckets[""] = Bucket( tag=None )

    #[-] deprecated
    def create_buckets( self, distributior=is_bucket ):
        candidates = [ tag.name for tag in get_unique_active_tags() ]
        for tag_name in candidates:
            if is_bucket( tag_name ):
                print "A bucket created for tag %s" % tag_name
                tag = Tag.objects.get( name=tag_name )
                self.buckets[tag_name] = Bucket( tag )

    #[-] deprecated
    def distribute_wishes( self ):
        for bucket in self.buckets.values():
            candidates = get_wishes_tagged_by( bucket.tag )
            for wish in candidates:
                bucket.add( wish )

    def distribute( self ):
        for wish in Wish.objects.all():
            self.to_bucket( wish )

    def to_bucket( self, wish ):
        for tag in wish.tags.all():
            if is_bucket( tag.name ):
                if not self.buckets.get(tag.name):
                    self.buckets[tag.name] = Bucket( tag )
                self.buckets[tag.name].add( wish )
                return self.buckets[tag.name]

        self.buckets[""].add( wish )
        return self.buckets[""]










class Bucket:
    def __init__( self, tag ):
        self.tag = tag
        self.wishes = []

    def add( self, other ):
        self.wishes.append( other )

    def extend( self, other_collection ):
        self.wishes.extend( other_collection )


class Strategy:
    def __init__( self, pool, rating_function, MIN_BOND_RATING=0.5 ):
        self.wishes = pool.wishes
        self.graph = network.Graph()

        self.rating_function = rating_function
        self.MIN_BOND_RATING = MIN_BOND_RATING

    def build_graph( self ):
        for wish in self.wishes:
            self.to_graph( wish )

    def to_graph( self, wish ):
        self.graph.add_node( wish )

        for node in self.graph.nodes():
            if wish.student != node.student:
                rating = self.rating_function(
                    wish.tags.all(),
                    node.tags.all()
                )

                if rating >= self.MIN_BOND_RATING:
                    self.graph.add_edge( wish, node, weight=rating )


    def create_group( self ):
        cliques = list( network.find_cliques( self.graph ) )
        groups = sorted( [c for c in cliques if len(c) > 1], key=lambda x: len(x) )
        counter = 0
        for g in groups:
            counter += 1
            print counter, g




if __name__ == "__main__":
    pool = Pool()
    #pool.create_buckets()
    #pool.distribute_wishes()

    pool.distribute()

    for bucket in pool.buckets.values():
        s = Strategy( bucket, jaccard )
        s.build_graph()
        try:
            print bucket.tag.name
        except AttributeError:
            pass
        s.create_group()


# registrerer gunstige opphopninger
# når de nærmer seg en bestemt tidsgrense: danne grupper uansett score

# tag1: bruker1, bruker2, bruker3
# tag2:          bruker2
# tag3:          bruker2
# tag4: bruker1,          bruker3, bruker4
# tag5: bruker5

# Tag 2,3,5 er valgt kun av en bruker. Derfor kan de ekskluderes fra matching
# Tag 4 og 1 har flere brukere, kan inkluderes i matching
# Bruker 1,3,4 matches i en gruppe pga interesse i 4 og 1

class Clique:
    def divide( self ):
        pass
        # 1. extract the remaining wishes from the original pool
        # 2. run the bonding with a reduced LOWER BOND LIMIT
        # 3. identify cliques in the current sub-pool

    """
    my.js must have features to fetch templated response views
    from specific views: for instance, the groups from
    a group view that parses the elements into a html.

    Each time a button or state change is triggered in the document
    the update_state function is called by javascript. The view is
    updated.

    The specific views generate the html code via template system,
    excluding the header and footer template (so that their
    output could be seamlessly integrated into the existing
    webpage.

    Therefore each restframework view must have a html-response
    method that serves the internal django templated data.

    A specific class of visual elements that update the the view.
    <a class="update">
    """