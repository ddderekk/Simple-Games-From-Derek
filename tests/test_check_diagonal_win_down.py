from unittest import TestCase
from connect_four.win_conditions.check_diagonal_win import check_diagonal_win_down


class TestCheckDiagonalWinDown(TestCase):
    def test_check_diagonal_win_down_type_error_board_not_dict(self):
        with self.assertRaises(TypeError):
            check_diagonal_win_down(board="{}", row=1, column=1)

    def test_check_diagonal_win_down_type_error_row_not_int(self):
        with self.assertRaises(TypeError):
            check_diagonal_win_down(board={}, row="1", column=1)

    def test_check_diagonal_win_down_type_error_column_not_dict(self):
        with self.assertRaises(TypeError):
            check_diagonal_win_down(board={}, row=1, column="1")

    def test_check_diagonal_win_standard_win(self):
        test_board = {(1, 1): '[O]', (1, 2): '[ ]', (1, 3): '[ ]', (1, 4): '[ ]', (2, 1): '[ ]',
                      (2, 2): '[O]', (2, 3): '[ ]', (2, 4): '[ ]', (3, 1): '[ ]', (3, 2): '[ ]', (3, 3): '[O]',
                      (3, 4): '[ ]', (4, 1): '[O]', (4, 2): '[ ]', (4, 3): '[ ]', (4, 4): '[O]'}
        self.assertTrue(check_diagonal_win_down(board=test_board, row=4, column=4))

    def test_check_diagonal_win_standard_no_win(self):
        test_board = {(1, 1): '[ ]', (1, 2): '[ ]', (1, 3): '[ ]', (1, 4): '[ ]', (2, 1): '[O]',
                      (2, 2): '[ ]', (2, 3): '[ ]', (2, 4): '[ ]', (3, 1): '[O]', (3, 2): '[O]', (3, 3): '[ ]',
                      (3, 4): '[ ]', (4, 1): '[O]', (4, 2): '[O]', (4, 3): '[O]', (4, 4): '[ ]'}
        self.assertFalse(check_diagonal_win_down(board=test_board, row=2, column=2))

    def test_check_diagonal_win_wrong_coordinate_chosen(self):
        test_board = {(1, 1): '[O]', (1, 2): '[ ]', (1, 3): '[ ]', (1, 4): '[ ]', (2, 1): '[ ]',
                      (2, 2): '[O]', (2, 3): '[ ]', (2, 4): '[ ]', (3, 1): '[ ]', (3, 2): '[ ]', (3, 3): '[O]',
                      (3, 4): '[ ]', (4, 1): '[O]', (4, 2): '[O]', (4, 3): '[O]', (4, 4): '[O]'}
        self.assertFalse(check_diagonal_win_down(board=test_board, row=3, column=2))

    def test_check_diagonal_win_top_row_empty_win(self):
        test_board = {(1, 1): '[ ]', (1, 2): '[ ]', (1, 3): '[ ]', (1, 4): '[ ]', (2, 1): '[O]',
                      (2, 2): '[ ]', (2, 3): '[ ]', (2, 4): '[ ]', (3, 1): '[ ]', (3, 2): '[O]', (3, 3): '[ ]', (3, 4):
                      '[ ]', (4, 1): '[O]', (4, 2): '[ ]', (4, 3): '[O]', (4, 4): '[ ]', (5, 1): '[ ]', (5, 2): '[ ]',
                      (5, 3): '[ ]', (5, 4): '[O]'}
        self.assertTrue(check_diagonal_win_down(board=test_board, row=5, column=4))

    def test_check_diagonal_win_row_not_in_board(self):
        test_board = {(1, 1): '[O]', (1, 2): '[O]', (1, 3): '[O]', (1, 4): '[O]', (2, 1): '[O]',
                      (2, 2): '[O]', (2, 3): '[O]', (2, 4): '[O]', (3, 1): '[O]', (3, 2): '[O]', (3, 3): '[O]',
                      (3, 4): '[O]', (4, 1): '[O]', (4, 2): '[O]', (4, 3): '[O]', (4, 4): '[O]'}
        self.assertFalse(check_diagonal_win_down(board=test_board, row=8, column=1))

    def test_check_diagonal_win_column_not_in_board(self):
        test_board = {(1, 1): '[0]', (1, 2): '[0]', (1, 3): '[O]', (1, 4): '[O]', (2, 1): '[O]',
                      (2, 2): '[O]', (2, 3): '[O]', (2, 4): '[O]', (3, 1): '[O]', (3, 2): '[O]', (3, 3): '[O]',
                      (3, 4): '[O]', (4, 1): '[O]', (4, 2): '[O]', (4, 3): '[O]', (4, 4): '[O]',
                      (5, 1): '[O]', (5, 2): '[O]', (5, 3): '[O]', (5, 4): '[O]'
                      }
        self.assertFalse(check_diagonal_win_down(board=test_board, row=3, column=10))

    def test_check_diagonal_win_board_empty_dict(self):
        self.assertFalse(check_diagonal_win_down(board={}, row=3, column=3))
