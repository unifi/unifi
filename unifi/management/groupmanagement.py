# -*- coding: utf8 -*-

"""
    The unifi API
"""
from student.models import Student, Wish
from tag.models import Tag
from group.models import Group
from usermanagement import UserManagement

class GroupManagement:
    """
        Takes care of group management
    """

    def __init__(self):
        self.user_management = UserManagement()

    def addGroup(self, wishes=[], students=[]):
        # [-] remove mutable values
        """
            Create a new group
            @param tags: the group tags
            @param students: the students belonging to this group
        """
        group = Group()
        group.save()

        for wish in wishes:
            group.wishes.add(wish)

        for student in students:
            if student is not None:
                group.students.add(student)

        return group

    def getStudents(self, group):
        """
            Get the students on a group
            @param group: the group
            @return: the students
        """

        return group.students

    def getTags(self, group):
        """
            Get the tags on a group
            @param group: the group
            @return: the tags
        """

        return group.tags

    def getGroups(self, student):
        """
            Get all groups that a student is part of
            @param student: the student
            @return: a set of groups
        """

        #if student is a string, get the student object
        student = self.user_management.getStudent(student)
        print student
        groups = []

        return [group for group in Group.objects.all() if student in group.students.all()]

    def flushGroups(self):
        """
            Delete all group objects
        """

        Group.objects.all().delete()
        print "Group table flushed"

