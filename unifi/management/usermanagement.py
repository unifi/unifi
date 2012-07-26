
"""
    The unifi API
"""
from student.models import Student
from oracle.models import Oracle
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

    def addStudent(self, usr):
        self.addUser(usr)
        self.updateUser(usr, "s")


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

    def getStudent(self, usr):
        """
            Get the student with username usr
            @param usr: the username
            @return: the student, or None if no student exists
        """

        try:
            return Student.objects.get(user=self.getUser(usr))
        except:
            return None

    def getOracle(self, usr):
        """
            Get the oracle with username usr
            @param usr: the username
            @return: the oracle, or None if no oracle exists
        """

        try:
            return Oracle.objects.get(user=self.getUser(usr))
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

        #o - oracle, s - student, r - restore (is_active = True)
        if not arg or arg[0] not in ['o', 's', 'r', 'student', 'oracle', 'restore']:
            print "Argument must be of type 'o', 's', or 'r', 'student', 'oracle', 'restore'"
            return

        usr = usr.strip()

        u = User.objects.get_or_create(username=usr)

        if arg[0] == 's' or arg[0] == 'student':
            s = Student.objects.get_or_create(user=u[0])
            print "User '%s' is now registered as student." % usr

        elif arg[0] == 'o' or arg[0] == 'oracle':
            try:
                s = Student.objects.get(user=u[0])
            except:
                pass

            o = Oracle.objects.get_or_create(user=u[0])
            print "User '%s' is now registered as oracle." % usr

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

