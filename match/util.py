#!/usr/bin/env python2.7

from __future__ import division
from itertools import combinations
from math import sqrt

from unifi.management import \
    tagmanagement, wishmanagement, usermanagement, groupmanagement

from wish.models import *

class Pool:
    """
    Ordering of pairs given by their index

    @param wishes    the list of wishes with at least one tag in each
    """
    def __init__( self, wishes ):
        self.wishes = wishes

    def pair( self, limit = 0.5 ):
        """
        @return     a list of pairs ordered by their quality index (score)
        """
        for p in self.active_pairs():
            score = p.sorensen_similarity()
            if score >= limit:
                yield ( score, p, p.wish_A.student, p.wish_B.student )



    def active_pairs( self ):
        for pair in combinations( self.active_wishes(), 2 ):
            yield Pair( pair[0], pair[1] )

    def active_wishes( self ):
        active_wishes = []
        for w in self.wishes:
            for t in self.active_tags():
                wish_tags = w.tags.all()
                if t in wish_tags:
                    active_wishes.append(w)

        return set(active_wishes)


    def active_tags( self ):
        """
        @return     a list of active tags
        """

        tags_in_wishes = set()

        for w in self.wishes:
            for t in w.tags.all():
                tags_in_wishes.add( t )

        return tags_in_wishes




class Pair:
    """
    Temporary Pair-container for algorithm development.
    """
    class Sample:
        def __init__( self, this, other ):
            self.this = set(this)
            self.other = set(other)

        def __call__( self ):
            return self.this

        def __len__( self ):
            return len( self.this )

        def __rsub__( self, other ):
            return self.this - other

        def __rsub__( self, other ):
            return other - self.this

        def __add__( self, other ):
            return self.this.union( other )

        def __radd__( self, other ):
            return self.__add__( other )

        def common( self ):
            return ( self.this & self.other )

        def uncommon( self ):
            return ( self.this ^ self.other )

        def complement(self):
            return self.other - self.this

        def own(self):
            return self.this - self.other

    def __init__( self, A, B ):
        self.wish_A = A
        self.wish_B = B
        self.A = self.Sample( A.tags.all(), B.tags.all() )
        self.B = self.Sample( B.tags.all(), A.tags.all() )

    def all( self ):
        """
        @return     union
        """
        return ( self.A() | self.B() )

    def common( self ):
        return ( self.A() & self.B() )

    def uncommon( self ):
        return ( self.A() ^ self.B() )

    def distance( self, insertion_cost=1, deletion_cost=1 ):
        """
        @return     the distance from A to B, mind that this is not
                    a commutative operation if insertion_cost != deletion_cost
        """
        # for e in a:
        #     if e not in b: # implies deletion from A
        #         score += deletion_cost

        # for e in b:
        #     if e not in a: # implies insertion into A
        #         score += insertion_cost

        return len( self.A.complement() ) * insertion_cost + \
               len( self.B.complement() ) * deletion_cost


    def inverse_distance( self, insertion_cost=1, deletion_cost=1 ):
        return len( self.B.complement() ) * insertion_cost +\
               len( self.A.complement() ) * deletion_cost

    # Similarity indices

    def sorensen_similarity( self ):
        return ( 2.0 * len( self.common()) ) / ( len(self.A) + len(self.B) )

    def tversky_similarity( self, alpha = 0.5, beta = 0.5 ):
        """
        @param alpha
        @param beta
        """
        numerator = len(self.common())
        denominator = len(self.common()) + alpha*len(self.A.own()) + beta*len(self.B.own())
        return numerator / denominator

    def jaccard_similarity( self ):
        return len(self.common()) / \
               len(self.all())

    def mountford_similarity( self ):
        result = 0.0
        numerator = 2.0 * len(self.common())
        denominator = 2.0 * len(self.A) * len(self.B) \
                      - (
                            ( len(self.A) + len(self.B) ) * len( self.common() )
                        )
        try:
            result = numerator / denominator
        except ZeroDivisionError:
            result = 0.0

        return result

if __name__ == "__main__":
    pass