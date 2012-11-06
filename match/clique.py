# -*- coding: utf8 -*-

from group.models import Group



class WishClique:
    def __init__( self, nodes ):
        self.nodes = nodes
        self.tags = self.update_tags()
        self.persons = self.update_persons()

    def __len__( self ):
        return len( self.nodes )

    def create_group( self ):
        new_group = Group()
        new_group.save()

        for person in self.persons:
            new_group.persons.add( person )

        new_group.save()

        for wish in self.nodes:
            wish.is_active = False
            new_group.wishes.add( wish )
            wish.save()

        new_group.save()

        return new_group


    def update_tags( self ):
        result = set()
        for n in self.nodes:
            for t in n.tags.all():
                result.add( t )
        self.tags = result
        return result

    def get_common_tags( self ):
        result = set()
        for n in self.nodes:
            if not len( result ):
                result = set( n.tags.all() )
            else:
                result.intersection_update( n.tags.all() )
        return result

    def get_missing_tags( self ):
        return self.tags.difference( self.get_common_tags() )

    def get_score( self ):
        score = 0.0
        try:
            score = len( self.get_common_tags() ) / float( len( self.tags ) )
        except ZeroDivisionError:
            pass
        return score

    def update_persons( self ):
        result = []
        for n in self.nodes:
            result.append( n.person )
        self.persons = result
        return result