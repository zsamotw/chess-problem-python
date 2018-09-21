class Board:
    def __init__(self, size):
        self.figures = []
        self.size = size

    def is_valid(self):
        return self.size > 0 and len(self.figures) < self.size * self.size

    def is_safe_for(self, figure):
        return all([(not other.is_attack(figure.x, figure.y)
                     and not figure.is_attack(other.x, other.y))
                    for other in self.figures])
