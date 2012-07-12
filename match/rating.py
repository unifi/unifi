#!/usr/bin/env python2.7

from __future__ import division



def jaccard( A, B ):
    A, B = set(A), set(B)
    return len( A.intersection(B) ) / \
           len( A.union(B) )

def tversky( A, B, alpha=1.0, beta=1.0 ):
    A, B = set(A), set(B)
    intersection = A.intersection(B)
    return ( len( intersection ) ) / \
           ( len( intersection ) + alpha * len( A-B ) + beta * len( B-A ) )

def dice( A, B ):
    A, B = set(A), set(B)
    intersection = A.intersection(B)
    return len(intersection) / \
           ( len(A) + len(B) )

def mountford( A, B ):
    A, B = set(A), set(B)
    intersection = A.intersection(B)
    return ( 2.0 * len(intersection) ) / \
           ( 2.0 * len(A) * len(B) - (len(A) + len(B)) * len( intersection) )

def sorensen( A, B ):
    A, B = set(A), set(B)
    intersection = A.intersection(B)
    return ( 2.0 * len( intersection )) / \
           ( len(A) + len(B) )

