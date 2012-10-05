#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

import re
import networkx as network
from group.models import Group
from person.models import *


def is_bucket( tag ):
    pattern = r'^\w{3}\d{4}$'
    return re.match( pattern, tag )

def get_unique_active_tags():
    from person.models import Wish

    unique_active_tags = set()
    for wish in Wish.objects.all():
        for tag in wish.tags.all():
            unique_active_tags.add( tag )

    return unique_active_tags

def get_wishes_tagged_by( tag ):
    from person.models import Wish
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





class Pool:
    def __init__( self ):
        self.buckets = dict()
        # creates the default bucket
        self.buckets[""] = Bucket( tag=None )
        self.distribute()

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
    def __init__( self, bucket, rating_function, MIN_BOND_RATING=0.5 ):
        self.wishes = bucket.wishes
        self.graph = network.Graph()
        self.rating_function = rating_function
        self.MIN_BOND_RATING = MIN_BOND_RATING

        self._build_graph()

    def __call__( self ):
        cliques = list( network.find_cliques( self.graph ) )
        groups = []

        for c in cliques:
            # excludes the cliques that have only one member
            if len(c) > 1:
                groups.append(c)

        groups = sorted( groups, key=lambda x: len(x) )

        return groups

    def _build_graph( self ):
        for wish in self.wishes:
            if wish.is_active:
                self._to_graph( wish )
        return self.graph

    def cliques( self ):
        candidates = list( network.find_cliques( self.graph ) )
        result = []
        for c in candidates:
            # excludes the cliques that have only one member
            if len(c) > 1:
                result.append(c)

        return result

    def create_groups( self ):
        wish_sets = sorted( self.cliques(), key=lambda x: len(x) )
        for ws in wish_sets:
            group = Group()
            group.save()
            for w in ws:
                group.persons.add( w.person )
                group.wishes.add( w )
                self._from_graph( w )
            group.save()


    def _to_graph( self, candidate ):
        # adds the candidate wish to the graph
        self.graph.add_node( candidate )
        # creates bonds if the candidate wish is compatible with
        # existing nodes of the graph
        for node in self.graph.nodes():
            rating = self._rate( candidate, node )
            if rating >= self.MIN_BOND_RATING:
                self.graph.add_edge( candidate, node, weight=rating )

    def _from_graph( self, candidate ):
        # self.wishes.remove( candidate )
        candidate.is_active = False
        candidate.save()
        self._build_graph()

    def _rate( self, this, other ):
        rating = 0.0
        if this.person != other.person:
            rating = self.rating_function( this.tags.all(), other.tags.all() )

        return rating

    def _dev_rate( self, this, other ):
        return self.rating_function( this.tags.all(), other.tags.all() )







# 1. extract the remaining wishes from the original pool
# 2. run the bonding with a reduced LOWER BOND LIMIT
# 3. identify cliques in the current sub-pool

# wishes in buckets have a default bonding right
# independent from their score
# so the bucket tags are stronger and yield greater
# compatibility score
# all wishes in the default bucket may be set together
# to groups, especially if the user does not
# provide any other tags in addition to the bucket tag

# har du lyst aa danne en helt ny gruppe, eller bli med i en
# eksisterende