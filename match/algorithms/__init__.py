#!/usr/bin/env python2.7

from match.algorithms.WishDispatcher import *
from multiprocessing import Process, Pool
from threading import Thread

MAX_GROUP_SIZE = 2
MIN_SCORE = 0.5 # (less == high likeness, more = low likeness)

WishDispatcher = WishDispatcher( MAX_GROUP_SIZE, MIN_SCORE )

#if not WishDispatcher.has_restored: #Restore buckets if first time run
#    WishDispatcher.restore_buckets()


# [/] temporary, threading in python is a myth
# class Dispatch(Thread):
    # def run( self ):
        # WishDispatcher()

# t = Dispatch()
# t.start()


# [!]

# def start_matching():
    # WishDispatcher()


# pool = Pool(1)
# pool.map( start_matching, [1] )

