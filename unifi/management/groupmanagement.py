# -*- coding: utf8 -*-

"""
    The unifi API
"""
from person.models import Person, Wish
from tag.models import Tag
from group.models import Group
from usermanagement import UserManagement

class GroupManagement:
    """
        Takes care of group management
    """

    def __init__(self):
        self.user_management = UserManagement()

    def addGroup(self, wishes=[], persons=[]):
        # [-] remove mutable values
        """
            Create a new group
            @param tags: the group tags
            @param persons: the persons belonging to this group
        """
        group = Group()
        group.save()

        for wish in wishes:
            group.wishes.add(wish)

        for person in persons:
            if person is not None:
                group.persons.add(person)

        return group

    def getPersons(self, group):
        """
            Get the persons on a group
            @param group: the group
            @return: the persons
        """

        return group.persons

    def getTags(self, group):
        """
            Get the tags on a group
            @param group: the group
            @return: the tags
        """

        return group.tags

    def getGroups(self, person):
        """
            Get all groups that a person is part of
            @param person: the person
            @return: a set of groups
        """

        #if person is a string, get the person object
        person = self.user_management.getPerson(person)
        print person
        groups = []

        return [group for group in Group.objects.all() if person in group.persons.all()]

    def flushGroups(self):
        """
            Delete all group objects
        """

        Group.objects.all().delete()
        print "Group table flushed"

