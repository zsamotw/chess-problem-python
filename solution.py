from board import Board
from timer import timer


@timer
def solution(size, figure_classes):
    initial = Board(size)
    boards = {initial}
    for f in figure_classes:
        boards_in_loop = set()
        for board in boards:
            boards_set = board.loop_for_new_boards(f)
            boards_in_loop |= boards_set
        boards = boards_in_loop
        print('for figure {} there are {} boards'.format(f, len(boards)))
    print('There are: {} results'.format(len(boards)))
    return boards
