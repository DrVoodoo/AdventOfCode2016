
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

# class Decryption(object):
#     """Used to validate decryption"""
#     def __init__(self):
#         self.valid_triangles = 0
#     def validate(self, values):
#         """Move one step on the pad"""
#         b_and_c = values[1] + values[2]
#         a_and_c = values[0] + values[2]
#         a_and_b = values[0] + values[1]
#         if values[0] < b_and_c and values[1] < a_and_c and values[2] < a_and_b:
#             self.valid_triangles = self.valid_triangles + 1
#     def count(self):
#         """Print the number of valid triangles"""
#         return self.valid_triangles

class DecryptionData(object):
    """Settings for one decryption line"""
    def __init__(self, data):
        data = data.translate(None, ' \n\t\r')
        rev = data[::-1]
        rev_check_sum = ""
        rev_sector_id = ""
        rev_name = ""
        step = 0
        for next_char in rev:
            if next_char == '[':
                step = 1
                continue
            if next_char == ']':
                continue
            if next_char == '-':
                step = 2
                continue
            if step == 0:
                rev_check_sum = rev_check_sum + next_char
            if step == 1:
                rev_sector_id = rev_sector_id + next_char
            if step == 2:
                rev_name = rev_name + next_char

        self.check_sum = rev_check_sum[::-1]
        self.sector_id = rev_sector_id[::-1]
        self.name = rev_name[::-1]
    def is_real_room(self):
        """Check if it is a real room"""
        values = dict()
        for sign in self.name:
            keys = values.keys()
            found = False
            for key in keys:
                if sign == key:
                    found = True
                    break
            if found:
                values[sign] = values[sign] + 1
            else:
                values[sign] = 1
        #print values
        #sorted = []
i = Instructions()
i.load('aoc04.txt')
NEXT = i.next()
# TRIANGLE = Triangle()
# ROW1 = None
# ROW2 = None
# ROW3 = None

while NEXT:
    DECDATA = DecryptionData(NEXT)
    DECDATA.is_real_room()
    NEXT = i.next()
    #P = re.compile(r'\W+')
    # VALUES = P.split(NEXT)
    # ROW1 = [int(x) for x in VALUES if x]
    # NEXT = i.next()
    # if not NEXT:
    #     break
    # P = re.compile(r'\W+')
    # VALUES = P.split(NEXT)
    # ROW2 = [int(x) for x in VALUES if x]
    # NEXT = i.next()
    # if not NEXT:
    #     break
    # P = re.compile(r'\W+')
    # VALUES = P.split(NEXT)
    # ROW3 = [int(x) for x in VALUES if x]
    # NEXT = i.next()
    # validate triangles
    #TRIANGLE.validate([ROW1[0], ROW2[0], ROW3[0]])
    #TRIANGLE.validate([ROW1[1], ROW2[1], ROW3[1]])
    #TRIANGLE.validate([ROW1[2], ROW2[2], ROW3[2]])
# print TRIANGLE.count()
