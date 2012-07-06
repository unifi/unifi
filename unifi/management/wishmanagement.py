
"""
    The unifi command line interface
"""
from student.models import Wish, Student
from tag.models import Tag
from django.contrib.auth.models import User
from usermanagement import UserManagement
from tagmanagement import TagManagement

class WishManagement:
    """
        Takes care of wish management (adding, removing, updating ...)
    """

    def __init__(self):
        self.user_management = UserManagement()
        self.tag_management = TagManagement()

    def addWish(self, student, tags):
        """
            Add a user
            @param student: the student's thats register a wish
            @param tags: wish tags
        """

        if not tags:
            print "Please specify at least one tag"
            return

        if student.__class__ == str:
            student = student.strip()
            student = self.user_management.getStudent(student)

        w = self.getWish(student, tags)

        if w != None:
            print "Wish for: %s exist" % student
            return w

        w = Wish()
        w.student=student
        w.save()

        for t in tags:
            try:
                t = self.tag_management.addTag(t)
                w.tags.add(t)
            except Tag.DoesNotExist:
                print "Tag %s does not exist" % t

        print "Wish added for user %s" % student

        return w

    def deleteWish(self, wish):
        """
            Delete a wish
        """

        wish.delete()

    def getWish(self, student, tags):
        """
            get a wish (and your dream will come true)
            @param student: the students username
            @param tags: a list with tag names
        """

        if student.__class__ == str:
            student = self.user_management.getStudent(student)

        wishes = Wish.objects.filter(student=student)

        for w in wishes:
            wishtags = [t.name_of_tag for t in w.tags.all()]

            if set (wishtags) == set (tags):
                return w

        #If no wish found
        return None

    def getAStudentWishes(self, student):
        """
            Get all the wishes for a given student
            @param student: the student
            @return: list of wishes
        """

        if student.__class__ == str:
            student = self.user_management.getStudent(student)

        return Wish.objects.filter(student=student)

    def getAllWishesWithTag(self, tag):
        """
            Get all wishes with a given tag
            @param tag: the tag
            @return: a list of wishes
        """

        if tag.__class__ == str:
            tag = self.tag_management.getTag(tag)

        if tag == None:
            return []

        return [wish for wish in Wish.objects.all() for t in wish.tags.all() if t == tag]

    def flush(self):
        """
            Removes all entries in the wish table
        """

        Wish.objects.all().delete()
        print "Wish table flushed"

