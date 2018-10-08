from board import Board
from copy import deepcopy
from timer import timer
from utils import get_empty_board


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
    empty_board = get_empty_board(size)
    for board in boards:
        board.print_board(deepcopy(empty_board))
    print('There are: {} boards as result.'.format(len(boards)))
    return boards
