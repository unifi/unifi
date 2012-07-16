#!/usr/bin/env python2.7

import random
from string import ascii_lowercase

class Generator:
    def __init__(self):
        self.path = ""



class TagGenerator(Generator):
    def __init__(self):
        pass


class SubjectTagGenerator(TagGenerator):
    def __init__( self, subject_number_length = 4 ):
        self.subject_number_length = subject_number_length
        self.prefixes = [ "INF", "MAT", "MAT-INF", "STK" ]
        pass

    def generate( self, quantity ):
        self.prefixes = [ prefix.upper() for prefix in self.prefixes ]

        def make_subject_code():
            number = "".join(
                [ str(random.randint(0,9))
                    for i in range(self.subject_number_length) ]
            )
            return "%s%s" % (random.choice( self.prefixes ), number)

        return [make_subject_code() for i in range(quantity)]


class LetterTagGenerator(TagGenerator):
    def generate( self, quantity ):
        output = []

        tag_length = ( quantity / len(ascii_lowercase) ) +1
        print tag_length, len(ascii_lowercase)
        for i in xrange(quantity):
            output.append(
                "".join( random.sample( ascii_lowercase, tag_length ) )
            )

        return output

class WordTagGenerator(TagGenerator):
    def generate( self, quantity,
                  uri="http://www.desiquintans.com/downloads/nounlist.txt" ):

        from urllib import urlopen
        data = urlopen( uri ).read().split("\n")

        return random.sample( data, quantity )




class StudentGenerator(Generator):
    def __init__( self, username_length = 7 ):
        self.username_length = username_length

    def generate( self, quantity ):
        output = []
        minimum_length_factor = 0.7

        def make_username(length):
            output = ""

            vowels = set( ["a", "e", "i", "o", "u"] )
            # [!] not platform independent
            consonants = set(ascii_lowercase).difference(vowels)

            vowels = list(vowels)
            consonants = list(consonants)

            while length != 0:
                output += random.choice(consonants)
                output += random.choice(vowels)
                length -= 2
                if length == 1:
                    output += random.choice(consonants)
                    break

            return output


        for i in range(quantity):
            username_length = random.randint(
                int(self.username_length * minimum_length_factor),
                self.username_length
            )
            output.append(
                "".join(make_username(username_length))
            )

        return output


class WishGenerator(Generator):
    def __init__(self, students, tags):
        self.students = students
        self.tags = tags

    def generate( self,
                  quantity=0,
                  min_tag_quantity=1,
                  max_tag_quantity=5,
                  unique=True ):

        """
        @param quantity             the number of wishes to be generated
        @param unique               'True' if there's only one wish per user

        """

        if min_tag_quantity > max_tag_quantity:
            max_tag_quantity = min_tag_quantity +5


        # sets the default quantity
        output = []
        if quantity is 0:
            quantity = len( self.students )

        if unique:
            candidates = random.sample( self.students, quantity )
            for c in candidates:
                tag_quantity = random.randint(
                    min_tag_quantity, max_tag_quantity
                )

                output.append(
                    ( c, random.sample( self.tags, tag_quantity ))
                )

        else:
            for c in xrange( 0, quantity ):
                user = random.choice( self.students )
                tag_quantity = random.randint(
                    min_tag_quantity, max_tag_quantity
                )

                output.append(
                    ( user, random.sample( self.tags, tag_quantity ) )
                )

        return output


if __name__ == "__main__":
    pass