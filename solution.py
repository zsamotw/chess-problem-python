from board import Board


def solution(size, figure_classes):
    initial = Board(size)
    boards = {initial}
    for f in figure_classes:
        print('boards in begining of loop for figure {}:\n {}'.format(
            f, boards))
        boards_in_loop = set()
        for board in boards:
            boards_set = board.loop_for_new_boards(f)
            boards_in_loop |= boards_set  # = boards_in_loop.union((boards_set))
        boards = boards_in_loop
        # print('boards with new figure {} length : {}: {}\n\n'.format(f, len(boards), boards))
    return boards
