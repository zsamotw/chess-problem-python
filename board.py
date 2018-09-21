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

    def loop_for_new_boards(self, figure_class):
        boards = []
        for x in range(1, self.size + 1):
            for y in range(1, self.size + 1):
                figure = figure_class(x, y)
                print(self.is_safe_for(figure))
                if self.is_safe_for(figure):
                    board = Board(self.size)
                    figures = self.figures[:].append(figure)
                    board.figures = figures
                    boards.append(board)
        return boards
