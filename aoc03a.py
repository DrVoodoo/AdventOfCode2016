
import re

class Instructions(object):
    """Advent of code load task instructions."""
    def __init__(self):
        self.instructions = None
    def load(self, name):
        """Load a file"""
        self.instructions = open(name, 'r')
    def next(self):
        """Read a new row with instructions"""
        return self.instructions.readline()
    def close(self):
        """Close current file"""
        self.instructions.close()

class Triangle(object):
    """Used to validate triangle values"""
    def __init__(self):
        self.valid_triangles = 0
    def validate(self, values):
        """Move one step on the pad"""
        b_and_c = values[1] + values[2]
        a_and_c = values[0] + values[2]
        a_and_b = values[0] + values[1]
        if values[0] < b_and_c and values[1] < a_and_c and values[2] < a_and_b:
            self.valid_triangles = self.valid_triangles + 1
    def count(self):
        """Print the number of valid triangles"""
        return self.valid_triangles

i = Instructions()
i.load('aoc03.txt')
NEXT = i.next()
TRIANGLE = Triangle()

while NEXT:
    P = re.compile(r'\W+')
    VALUES = P.split(NEXT)
    TRIANGLE.validate([int(x) for x in VALUES if x])
    NEXT = i.next()

print TRIANGLE.count()
