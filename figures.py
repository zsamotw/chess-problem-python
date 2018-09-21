class Rook:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_attack(self, x, y):
        return self.x == x or self.y == y

    def __repr__(self):
        return 'R({}, {})'.format(self.x, self.y)


class Knight:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_attack(self, x, y):
        return (abs(self.x - x) == 1
                and abs(self.y - y) == 2) or (abs(self.x - x) == 2
                                              and abs(self.y - y) == 1)

    def __repr__(self):
        return 'Kn({}, {})'.format(self.x, self.y)


class Bishop:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_attack(self, x, y):
        return abs(self.x - x) == abs(self.y - y)

    def __repr__(self):
        return 'B({}, {})'.format(self.x, self.y)


class Queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_attack(self, x, y):
        return (
            abs(self.x - x) == abs(self.y - y)) or self.x == x or self.y == y

    def __repr__(self):
        return 'Q({}, {})'.format(self.x, self.y)


class King:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_attack(self, x, y):
        return abs(self.x - x) <= 1 and abs(self.y - y) <= 1

    def __repr__(self):
        return 'K({}, {})'.format(self.x, self.y)
