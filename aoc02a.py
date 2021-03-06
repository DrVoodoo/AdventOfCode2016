
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

class Keypad(object):
    """Keypad to simulate every row"""
    def __init__(self):
        self.pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.direction = ''
        self.x_pos = 1
        self.y_pos = 1
    def move(self, direction):
        """Move one step on the pad"""
        if direction == 'U' and self.y_pos > 0:
            self.y_pos = self.y_pos - 1
        if direction == 'D' and self.y_pos < 2:
            self.y_pos = self.y_pos + 1
        if direction == 'L' and self.x_pos > 0:
            self.x_pos = self.x_pos - 1
        if direction == 'R' and self.x_pos < 2:
            self.x_pos = self.x_pos + 1
        #print direction, self.x_pos, self.y_pos
        self.direction = direction
    def code(self):
        """Get current keypad code"""
        return self.pad[self.y_pos][self.x_pos]

i = Instructions()
i.load('aoc02.txt')
NEXT = i.next()
KEYPAD = Keypad()

while NEXT:
    for c in NEXT:
        KEYPAD.move(c)
    print KEYPAD.code()
    NEXT = i.next()
    