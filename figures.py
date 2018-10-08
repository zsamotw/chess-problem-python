class Figure:
    __slots__ = ['__x', '__y']

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return ((self.x == other.x) and (self.y == other.y))
        else:
            return False

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.__repr__())


class Rook(Figure):
    __slots__ = ['__x', '__y']

    def is_attack(self, x, y):
        return self.x == x or self.y == y

    def __repr__(self):
        return 'R({}, {})'.format(self.x, self.y)

    def __str__(self):
        return 'R'


class Knight(Figure):
    __slots__ = ['__x', '__y']

    def is_attack(self, x, y):
        return (abs(self.x - x) == 1 and abs(self.y - y) == 2) or (
            abs(self.x - x) == 2 and abs(self.y - y) == 1) or (self.x == x
                                                               and self.y == y)

    def __repr__(self):
        return 'N({}, {})'.format(self.x, self.y)

    def __str__(self):
        return 'N'


class Bishop(Figure):
    __slots__ = ['__x', '__y']

    def is_attack(self, x, y):
        return abs(self.x - x) == abs(self.y - y)

    def __repr__(self):
        return 'B({}, {})'.format(self.x, self.y)

    def __str__(self):
        return 'B'


class Queen(Figure):
    __slots__ = ['__x', '__y']

    def is_attack(self, x, y):
        return (
            abs(self.x - x) == abs(self.y - y)) or self.x == x or self.y == y

    def __repr__(self):
        return 'Q({}, {})'.format(self.x, self.y)

    def __str__(self):
        return 'Q'


class King(Figure):
    __slots__ = ['__x', '__y']

    def is_attack(self, x, y):
        return abs(self.x - x) <= 1 and abs(self.y - y) <= 1

    def __repr__(self):
        return 'K({}, {})'.format(self.x, self.y)

    def __str__(self):
        return 'K'
