from board import Board
from figures import Bishop, King, Knight, Rook, Queen
from solution import solution


class TestSolution:
    def test_solution_for_board_2_and_1_rook(self):
        boards = solution(2, [Rook])
        assert len(boards) is 4

    def test_solution_for_board_3_and_2_kings_1_rook(self):
        boards = solution(3, [King, King, Rook])
        assert len(boards) is 4

    def test_solution_for_board_4_and_2_rooks_4_knight(self):
        boards = solution(3, [Rook, Rook, Knight, Knight, Knight, Knight])
        assert len(boards) is 8

    def test_solution_for_board_3_and_2_kings_1_rook_fig(self):
        boards = solution(3, [King, King, Rook])
        b1 = Board(3)
        b1.figures = [King(1, 1), King(3, 1), Rook(2, 3)]

        b2 = Board(3)
        b2.figures = [King(1, 1), King(1, 3), Rook(3, 2)]

        b3 = Board(3)
        b3.figures = [King(3, 1), King(3, 3), Rook(1, 2)]

        b4 = Board(3)
        b4.figures = [King(1, 3), King(3, 3), Rook(2, 1)]

        assert boards == {b1, b2, b3, b4}
