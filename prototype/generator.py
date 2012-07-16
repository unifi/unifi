#!/usr/bin/env python2.7

import random
from string import ascii_lowercase

# [!] in command-line mode, generates a single wish PER USER,
# but allows random duplicate usernames

# [*] Data is not shuffled, the user occurrence has the same ordering as the
# wish occurrence.

class TestDataGenerator:

    def __init__(self, username_length=6, path="gen/test/"):
        self.username_length = int(username_length)
        self.path = path
        self.subject_number_max_length = 4

    def generate_students(self, quantity):
        output = []
        minimum_length_factor = 0.7

        def make_username(length):
            output = ""

            vowels = set(["a", "e", "i", "o", "u"])
            consonants = set(ascii_lowercase).difference(vowels) # [!] not platform independent

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

    def generate_tags(self, quantity):
        subject_prefixes = [ "INF" ]
        subject_prefixes = [ prefix.upper() for prefix in subject_prefixes ]

        def make_subject_code():
            number = "".join([ str(random.randint(0,9))
                               for i in range(self.subject_number_max_length)])
            return "%s%s" % (random.choice(subject_prefixes), number)

        return [make_subject_code() for i in range(quantity)]


    def generate_wishes(self, students, tags, quantity=None, max_tag_quantity=6, min_tag_quantity=3):

        if min_tag_quantity > max_tag_quantity:
            temp = min_tag_quantity
            min_tag_quantity = max_tag_quantity
            max_tag_quantity = temp

        output = []
        if quantity is None:
            quantity = len(students)

        for c in xrange(0, quantity):
            user = random.choice( students )
            tag_quantity = random.randint( 3, max_tag_quantity )
            output.append(
                ( user, random.sample(tags, tag_quantity) )
            )

        return output




if __name__ == "__main__":

    generator = TestDataGenerator( raw_input("Username length: ") )
    students = generator.generate_students( int(raw_input( "User quantity: " )) )

    if "y" in raw_input("Save USERS to file? (y/n): "):
        with open( "./" + generator.path + "users.dat", "w" ) as out:
            out.write( "\n".join(students) )

    tags = generator.generate_tags( int(raw_input( "Tag quantity: " )) )

    if "y" in raw_input("Save TAGS to file? (y/n): "):
        with open( "./" + generator.path + "tags.dat", "w" ) as out:
            out.write( "\n".join(tags) )

    print "(make sure to specify both values, or defaults will be set)"
    min_tag_n = raw_input("Min-imum number of tags for each user: ")
    max_tag_n = raw_input("Max-imum number of tags for each user: ")

    # [!] FIX: defaults only when both are empty
    if min_tag_n != "" and max_tag_n != "":
        wishes = generator.generate_wishes( students, tags, int(max_tag_n), int(min_tag_n) )
    else:
        wishes = generator.generate_wishes( students, tags )

    if "y" in raw_input("Save WISHES to file? (y/n): "):
        with open( "./" + generator.path + "wishes.dat", "w" ) as out:
            for username,tags in wishes:
                out.write( "%s %s\n" % (username," ".join(tags)) )

