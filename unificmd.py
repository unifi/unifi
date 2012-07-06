#!/usr/bin/env python2.7

#TODO: implement group management
#Remove print statements from the different managers?

import getopt, sys

"""
    Unifi API
"""

class apidraft:

    def __init__(self):
        self.user_management = UserManagement()
        self.tag_management = TagManagement()
        self.group_management = GroupManagement()
        self.wish_management = WishManagement()

    def main(self, argv):
        """
            parse argv and execute the command(s)
        """
        try:
            opts, args = getopt.getopt(argv[1:],
                "hu:g:t:w:",
                [
                    "help",
                    "adduser=",
                    "du=",
                    "uu=",
                    "updateuser=",
                    "deleteuser=",
                    "flushusers",
                    "addtag=",
                    "flushtags",
                    "addwish=",
                    "flushwishes",
                    "populate",
                    "test"
                ]
            )
        except getopt.GetoptError, err:
            # print help information and exit:
            print str(err) # will print something like "option -f not recognized"
            print "%s --help for usage" % sys.argv[0]
            sys.exit(2)

        if len(opts) == 0:
            print "Remember the '--' before command!"
            sys.exit(1)

        for o, a in opts:

            if o in ("-h", "--help"):
                self.usage()
                sys.exit()

            elif o in ("-u", "--adduser"):
                self.adduser(a)
            elif o in ("-g", "--addgroup"):
                print "Group management not implemented yet!"
            elif o in ("--du", "--deleteuser"):
                self.deleteuser(a)
            elif o in ("--flushusers"):
                self.user_management.flush()
            elif o in ("--uu", "--updateuser"):
                self.updateuser(a, args)
            elif o in ("-t", "--addtag"):
                self.addtag(a)
            elif o in ("--flushtags"):
                self.tag_management.flush()
            elif o in ("-w", "--addwish"):
                self.addwish(a, args)
            elif o in ("--flushwishes"):
                self.wish_management.flush()

            else:
                assert False, "unhandled option"

    def adduser(self, in_user):

        """
            Add a user to the database
            @param in_user: the user to be added, can be a file or a single username
        """
        try:
            #argument is a file of users
            f = open(in_user, 'r')
            for usr in f:
                self.user_management.addUser(usr)

            f.close()
        except IOError:
            #Argument is a single user
            self.user_management.addUser(in_user)

    def deleteuser(self, in_user):
        """
            remove a user from the database
            @param in_user: the user to delete
        """

        try:
            #argument is a file of users
            f = open(in_user, 'r')
            for usr in f:
                self.user_management.deleteUser(usr)
        except IOError:
            self.user_management.deleteUser(in_user)


    def updateuser(self, in_user, args):
        """
            Update a user
            @param in_user: the user to update
            @param args: the update arguments
        """

        try:
            #argument is a file of users
            f = open(in_user, 'r')
            for usr in f:
                self.user_management.updateUser(usr, args)
        except IOError:
                self.user_management.updateUser(in_user, args)

    def addtag(self, in_tag):

        """
            Add a user to the database
            @param in_user: the user to be added, can be a file or a single username
        """
        try:
            #argument is a file of users
            f = open(in_tag, 'r')
            for tag in f:
                self.tag_management.addTag(tag)

            f.close()
        except IOError:
            #Argument is a single user
            self.tag_management.addTag(in_tag)

    def addwish(self, student, tags):

        try:
            #argument is a file of users
            f = open(student, 'r')
            for wishline in f:

                wishline = wishline.strip().split()
                studline = wishline[0]
                tagsline = wishline[1:]
                self.wish_management.addWish(studline, tagsline)

            f.close()
        except IOError:
            #Argument is a single user
            self.wish_management.addWish(student, tags)


    def match(self):
        pass

    def populate(self):
        pass

    def usage(self):
        """
        Print usage
        """

        print "Usage: %s [subcommand] [args] \n" % sys.argv[0]
        print "Help:"
        print "    -h --help\tto show this help and exit\n"
        print "Type '%s [subcommand] -h, --help for help on a specific" + \
              "subcommand (not impl. yet)\n"
        print "Available subcommands"

        print "[User]"
        print "\t-u,\t--adduser\t<user>"
        print "\t--du,\t--deleteuser\t<user>"
        print "\t--uu,\t--updateuser\t<user> <s/o/r>"
        print "\t--flushusers\tflush user table\n"

        print "[Tags]"
        print "\t-t,\t--addtag\t<tag>"
        print "\t--flushtags \tflush tag table\n"

        print "[Wish]"
        print "\t-w,\t--addwish\t<student> <tag(s)>"
        print "\t--flushwishes\tflush wish table\n"

        print "[Group]"
        print "Group management not yet implemented"



if __name__ == "__main__":
    """
        If run as standalone program
    """
    if len(sys.argv) <= 1:
        print "type 'python %s -h,  --help'" % sys.argv[0]
        sys.exit(1)


    # Have to set DJANGO_SETTINGS_MODULE when run as standalone program
    # to get access to modules
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'kgen.settings'

    from mvp.management.usermanagement  import UserManagement
    from mvp.management.tagmanagement   import TagManagement
    from mvp.management.groupmanagement import GroupManagement
    from mvp.management.wishmanagement  import WishManagement

    apidraft = apidraft()
    apidraft.main(sys.argv)
