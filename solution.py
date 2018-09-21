from board import Board


def solution(size, figure_classes):
    initial = Board(size)
    boards = {initial}
    for f in figure_classes:
        boards_in_loop = set()
        for board in boards:
            boards_set = board.loop_for_new_boards(f)
            boards_in_loop = boards_in_loop.union((boards_set))

        boards = boards_in_loop
    return boards
