from math import copysign


class Knot:
    def __init__(self, knot_id=None, x=0, y=0):
        self.x = x
        self.y = y
        self.id = knot_id

    def move(self, direction):
        if direction == 'U':
            self.y += 1
        elif direction == 'D':
            self.y -= 1
        elif direction == 'R':
            self.x += 1
        elif direction == 'L':
            self.x -= 1

    def overlap(self, other):
        return self.x == other.x and self.y == other.y

    def distance1(self, other):
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    def __repr__(self):
        return f"{self.x} {self.y}"


class Rope:
    def __init__(self, head=Knot(), tail=Knot()):
        self.head = head
        self.tail = tail
        self.tail_history = [(head.x, head.y)]

    def move_head(self, direction):
        self.head.move(direction)
        self.move_tail()

    @staticmethod
    def sign(x):
        return copysign(1, x)

    def move_tail(self):
        if not (self.head.overlap(self.tail) or self.head.distance1(self.tail)):
            x_sign = self.sign(self.head.x - self.tail.x)
            y_sign = self.sign(self.head.y - self.tail.y)
            if self.head.y != self.tail.y and self.head.x != self.tail.x:
                self.tail.x += int(x_sign)
                self.tail.y += int(y_sign)
            else:
                if self.head.x - self.tail.x != 0:
                    self.tail.x += int(x_sign)
                else:
                    self.tail.y += int(y_sign)

        self.tail_history.append((self.tail.x, self.tail.y))

    def print_knots_id(self):
        print(self.head.id, self.tail.id)

    def __repr__(self):
        return f"{repr(self.head)}-{repr(self.tail)}"


class BigRope:
    def __init__(self, size, x=0, y=0):
        self.ropes = []
        self.knots = []
        current_tail = Knot(1, x, y)
        current_head = Knot(0, x, y)
        self.knots.append(current_head)
        for i in range(size - 1):
            self.ropes.append(Rope(current_head, current_tail))
            current_head = current_tail
            current_tail = Knot(i + 2, x, y)
            self.knots.append(current_head)

    def move(self, direction):
        self.ropes[0].move_head(direction)
        for rope in self.ropes[1:]:
            rope.move_tail()

    def get_last_history(self):
        return self.ropes[-1].tail_history

    def display_grid(self, range_min, range_max):
        for y in range(range_max, range_min - 1, -1):
            line = ''
            for x in range(range_min, range_max + 1):
                test = True
                for knot in self.knots:
                    if knot.x == x and knot.y == y:
                        line += str(knot.id)
                        test = False
                        break
                if test:
                    line += '.'
            print(line)

    def __repr__(self):
        return ' | '.join([repr(rope) for rope in self.ropes])
