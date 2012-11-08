# -*- coding: utf8 -*-

"""
    The unifi API
"""
from person.models import Wish, Person
from tag.models import Tag
from usermanagement import UserManagement
from tagmanagement import TagManagement

class WishManagement:
    """
        Takes care of wish management (adding, removing, updating ...)
    """

    def __init__(self):
        self.user_management = UserManagement()
        self.tag_management = TagManagement()

    def addWish(self, person, tags, courses = None):
        """
            Add a user
            @param person: the person's thats register a wish
            @param tags: wish tags
            @return: the created wish
        """

        if not tags:
            return

        if person.__class__ == str:
            person = person.strip()
            person = self.user_management.getPerson(person)

        w = self.getWish(person, tags)

        if w is not None:
            print "Wish for: %s exist" % person
            return w

        w = Wish()
        w.person=person
        w.save()

        for t in tags:
            try:
                t = self.tag_management.addTag(t)
                w.tags.add(t)
            except Tag.DoesNotExist:
                print "Tag %s does not exist" % t

        print "Wish( person={0},\n\ttags=[{1}]\n)".format(
            person,
            ", ".join(tags)
        )

        return w

    def deleteWish(self, wish):
        """
            Delete a wish from the database
            @param wish: the wish to remove
        """

        wish.delete()

    def getWish(self, person, tags):
        """
            Return the wish (or None, if the wish doesnt exist) with the given person and tags
            @param person: the persons username
            @param tags: a list with tag names
        """

        if person.__class__ == str:
            person = self.user_management.getPerson(person)

        wishes = Wish.objects.filter(person=person)

        for w in wishes:
            wishtags = [t.name for t in w.tags.all()]

            if set (wishtags) == set (tags):
                return w

        #If no wish found
        return None

    def getAPersonWishes(self, person):
        """
            Get all the wishes for a given person
            @param person: the person
            @return: list of wishes
        """

        if person.__class__ == str:
            person = self.user_management.getPerson(person)

        return Wish.objects.filter(person=person)

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

