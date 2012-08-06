# -*- coding: utf8 -*-

"""
    The unifi API
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

    def addWish(self, student, tags, courses = None):
        """
            Add a user
            @param student: the student's thats register a wish
            @param tags: wish tags
            @return: the created wish
        """
        from match.algorithms import *

        if not tags:
            return

        if student.__class__ == str:
            student = student.strip()
            student = self.user_management.getStudent(student)

        w = self.getWish(student, tags)

        if w is not None:
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
#        from match.algorithms import *

        #add to correct bucket
        if courses is None:
            courses = WishDispatcher.extract_course_tag(tags)

        #No course - "default" bucket
        if not len(courses):
            WishDispatcher.add_wish_to_bucket(w, "default")
        else:
            WishDispatcher.add_wish_to_bucket(w, courses[0])

        return w

    def deleteWish(self, wish):
        """
            Delete a wish from the database
            @param wish: the wish to remove
        """

        wish.delete()

    def getWish(self, student, tags):
        """
            Return the wish (or None, if the wish doesnt exist) with the given student and tags
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

        if tag is None:
            return []

        return [wish for wish in Wish.objects.all() for t in wish.tags.all() if t == tag]

    def flush(self):
        """
            Removes all entries in the wish table
        """

        Wish.objects.all().delete()
        print "Wish table flushed"

