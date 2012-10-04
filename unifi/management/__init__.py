#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from tagmanagement import *
from groupmanagement import *
from usermanagement import *
from wishmanagement import *

WishManager     =   WishManagement()
GroupManager    =   GroupManagement()
UserManager     =   UserManagement()
TagManager      =   TagManagement()

class Management:

    VERBOSE = False

    def out( self, message ):
        if self.VERBOSE:
            print message