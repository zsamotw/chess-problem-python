from figures import (Rook, Knight, Bishop, Queen, King)


class TestFigures:
    def setup_class(self):
        self.r = Rook(4, 4)
        self.kn = Knight(4, 4)
        self.b = Bishop(4, 4)
        self.q = Queen(4, 4)
        self.k = King(4, 4)

    def test_Rook_is_attack_true_horiz(self):
        assert self.r.is_attack(4, 8)

    def test_Rook_is_attack_true_vert(self):
        assert self.r.is_attack(8, 4)

    def test_Rook_is_attack_false(self):
        assert self.r.is_attack(1, 2) is False

    def test_Knight_is_attack_true(self):
        fields = [(3, 2), (5, 2), (2, 3), (6, 3), (2, 5), (6, 5), (3, 6), (5,
                                                                           6)]
        res_table = [self.kn.is_attack(*field) for field in fields]
        assert all(res_table)

    def test_Knight_is_attack_false(self):
        fields = [(2, 2), (4, 3), (6, 2), (2, 4), (3, 4), (5, 4), (2, 6), (4,
                                                                           7)]
        res_table = [not self.kn.is_attack(*field) for field in fields]
        assert all(res_table)

    def test_bishop_is_attack_true(self):
        fields = [(3, 3), (5, 5), (5, 3), (3, 5), (2, 2), (6, 2)]
        res_table = [self.b.is_attack(*field) for field in fields]
        assert all(res_table)

    def test_bishop_is_attack_false(self):
        fields = [(4, 3), (5, 4), (4, 5), (3, 4), (4, 2), (3, 6)]
        res_table = [not self.b.is_attack(*field) for field in fields]
        assert all(res_table)

    def test_queen_is_attack_true(self):
        fields = [(3, 3), (5, 5), (5, 3), (3, 5), (2, 2), (6, 2), (8, 4), (4,
                                                                           8)]
        res_table = [self.q.is_attack(*field) for field in fields]
        assert all(res_table)

    def test_queen_is_attack_false(self):
        fields = [(1, 2), (2, 3), (3, 2), (5, 2), (6, 5), (5, 7), (2, 7)]
        res_table = [not self.q.is_attack(*field) for field in fields]
        assert all(res_table)

    def test_king_is_attack_true(self):
        fields = [(x, y) for x in range(3, 6) for y in range(3, 6)]
        res_table = [self.k.is_attack(*field) for field in fields]
        assert all(res_table)

    def test_king_is_attack_false(self):
        fields = [(2, 2), (5, 2), (4, 2), (4, 6), (6, 6)]
        res_table = [not self.k.is_attack(*field) for field in fields]
        assert all(res_table)
