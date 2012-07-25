#!/usr/bin/env python2.7
from match.algorithms.WishDispatcher import *
from multiprocessing import Process, Pool
from threading import Thread
from unifi.unifi_project_settings import MAX_GROUP_SIZE, MIN_SCORE

WishDispatcher = WishDispatcher(MAX_GROUP_SIZE, MIN_SCORE)

if not WishDispatcher.has_restored: #Restore buckets if first time run
    WishDispatcher.restore_buckets()


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

