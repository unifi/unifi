# -*- coding: utf8 -*-

"""
    The unifi API
"""
from tag.models import Tag


class TagManagement:
    """
        Takes care of tag management (adding, removing, getting ...)
    """
    def __init__(self):

        pass

    def addTag(self, tag):
        """
            Add a user
            @param usr: the user to be added
        """
        tag = tag.strip() #remove whitespace
        t = Tag.objects.get_or_create(name_of_tag=tag)[0]
        # print "tag '%s' added!" % tag
        return t

    def deleteTag(self, tag):
        """
            Delete a tag (or rather, set the is_active flag to False so
            any foreign keys to users won't break
            @param usr: the user to remove
        """
        try:
            Tag.objects.get(name_of_tag=name).delete()
        except Tag.DoesNotExist:
            pass

    def getTag(self, name):
        """
            Return a tag
            @param name: the name of the tag
        """

        try:
            return Tag.objects.get(name_of_tag=name)
        except Tag.DoesNotExist:
            return None

    def getStudentsWithTag(self, tag):
        """
            Get all students with a given tag
            @param tag: the tag
        """
        from unifi.management.wishmanagement import WishManagement
        self.wish_management = WishManagement()
        wishes = self.wish_management.getAllWishesWithTag(tag)
        return [w.student for w in wishes]

    def flush(self):
        """
            Removes all entries in the tag table (and not just is_active=False)
        """

        Tag.objects.all().delete()
        print "Tag table flushed"
