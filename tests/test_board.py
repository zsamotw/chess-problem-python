from board import Board
from figures import Bishop, King, Knight, Rook, Queen


class TestBoard:
    def test_board_with_0_size_is_valid(self):
        board = Board(0)
        assert board.is_valid() is False

    def test_board_with_more_figures_then_fields_is_valid(self):
        board = Board(1)
        board.figures = [Rook(1, 1), King(1, 1)]
        assert board.is_valid() is False

    def test_board_with_no_figures_is_safe_for_Rook(self):
        board = Board(3)
        rook = Rook(1, 1)
        assert board.is_safe_for(rook)

    def test_board_with_some_figures_is_safe_for_Rook(self):
        board = Board(5)
        board.figures = [Knight(1, 1), Bishop(1, 5), King(5, 5)]
        rook = Rook(4, 3)
        assert board.is_safe_for(rook)

    def test_board_with_queen_is_not_safe_for_rook(self):
        board = Board(4)
        board.figures = [Queen(1, 1)]
        rook = Rook(2, 2)
        assert board.is_safe_for(rook) is False

    def test_board_when_adding_rook_break_figure_on_board(self):
        board = Board(4)
        board.figures = [Knight(1, 1)]
        rook = Rook(1, 4)
        assert board.is_safe_for(rook) is False

    def test_board_when_adding_rook_is_not_safe_on_board(self):
        board = Board(5)
        board.figures = [Knight(1, 1), Bishop(1, 5), King(5, 5)]
        rook = Rook(5, 4)
        assert board.is_safe_for(rook) is False

    def test_loop_for_new_boards_over_empty_board(self):
        board = Board(2)
        rook = Rook
        boards = board.loop_for_new_boards(rook)
        assert len(boards) is 4

    def test_loop_for_new_boards_over_board_with_Knight(self):
        board = Board(3)
        board.figures = [Knight(1, 1)]
        rook = Rook
        boards = board.loop_for_new_boards(rook)
        assert len(boards) is 2

    def test_loop_for_new_boards_over_board_with_two_rooks(self):
        board = Board(5)
        board.figures = [Rook(1, 1), Rook(5, 5)]
        rook = Rook
        boards = board.loop_for_new_boards(rook)
        assert len(boards) is 9
