# -*- coding: utf8 -*-

"""
    The unifi API
"""
from person.models import Person
from django.contrib.auth.models import User

class UserManagement:
    """
        Takes care of user management (adding, removing, updating ...)
    """

    def __init__(self):
        pass

    def addUser(self, usr):
        """
            Add a user
            @param usr: the user to be added
            @return: the created user
        """
        usr = usr.strip() #remove whitespace

        try:
            u = User.objects.get(username=usr)
            print "User '%s' exists in database." % usr
        except:
            u = User.objects.create_user(usr, password="123")
            print "user %s added!" % usr
            if not u.is_active:
                print "If the user at some point was deleted "\
                    "you want to do a user restore instead of add"

        return u

    def addPerson(self, usr):
        self.addUser(usr)
        self.updateUser(usr, "s")
        return self.getPerson(usr)


    def getUser(self, usr):
        """
            Get the user with username usr
            @param usr: the username
            @return: the user, or None if no user exists
        """

        usr = usr.strip() #remove whitespace
        try:
            return User.objects.get(username=usr)
        except User.DoesNotExist:
            return None

    def getPerson(self, usr):
        """
            Get the person with username usr
            @param usr: the username
            @return: the person, or None if no person exists
        """

        try:
            return Person.objects.get(user=self.getUser(usr))
        except:
            return None


    def deleteUser(self, usr):
        """
            Delete a user (or rather, set the is_active flag to False so
            any foreign keys to users won't break
            @param usr: the user to remove
        """

        usr = usr.strip() #remove whitespace
        try:
            u = User.objects.get(username=usr)
            u.is_active=False
            u.save()
            print "user %s removed (is_active=False)" % usr
        except User.DoesNotExist:
            print "User '%s' does not exists in database." % usr

    def updateUser(self, usr, arg):
        """
            Update an user
            @param usr: the user(name) to update
            @param: arg: info to be updated
        """

        # s - person, r - restore (is_active = True)
        if not arg or arg[0] not in ['s', 'r', 'person', 'restore']:
            print "Argument must be of type 's', or 'r', 'person', 'restore'"
            return

        usr = usr.strip()

        u = User.objects.get_or_create(username=usr)

        if arg[0] == 's' or arg[0] == 'person':
            s = Person.objects.get_or_create(user=u[0])
            print "User '%s' is now registered as person." % usr

        else: #arg is now r
            u[0].is_active = True
            u[0].save()
            print "User '%s' is now restored (is_active=True)." % usr

    def flush(self):
        """
            Removes all entries in the user table (and not just is_active=False)
        """

        User.objects.all().delete()
        print "User table flushed"

