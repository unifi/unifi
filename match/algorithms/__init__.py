#!/usr/bin/env python2.7
from match.algorithms.WishDispatcher import *
from multiprocessing import Process, Pool
from threading import Thread

WishDispatcher = WishDispatcher()


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

