# This module explores the definition and use of a Python class. Python unit
# testing is also introduced.

class Person(object):

    def __init__(self, given_name, sir_name):
        self.given_name = given_name
        self.sir_name = sir_name

    def name(self):
        return "%s %s" % (self.given_name, self.sir_name)


import unittest

class PersonTest(unittest.TestCase):

    def testConstructor(self):
        p = Person("Josh", "Calahan")
        self.assertEquals("Josh", p.given_name)
        self.assertEquals("Calahan", p.sir_name)

    def testAccessor(self):
        p = Person("Josh", "Calahan")
        self.assertEquals("Josh Calahan", p.name())

unittest.main()
