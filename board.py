class Board:
    def __init__(self, size):
        self.figures = set()
        self.size = size

    def is_valid(self):
        return self.size > 0 and len(self.figures) < self.size * self.size

    def is_safe_for(self, figure):
        return all([(not other.is_attack(figure.x, figure.y)
                     and not figure.is_attack(other.x, other.y))
                    for other in self.figures])

    def loop_for_new_boards(self, figure_class):
        boards = set()
        for x in range(1, self.size + 1):
            for y in range(1, self.size + 1):
                figure = figure_class(x, y)
                if self.is_safe_for(figure):
                    board = Board(self.size)
                    figures = set(self.figures)
                    figures.add(figure)
                    board.figures = figures
                    boards.add(board)
        return boards

    def __repr__(self):
        return 'Board {} x {} figures: {}'.format(self.size, self.size,
                                                  self.figures)

    def __eq__(self, other):
        if isinstance(other, Board):
            return ((self.figures == other.figures)
                    and (self.size == other.size))
        else:
            return False

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.__repr__())
