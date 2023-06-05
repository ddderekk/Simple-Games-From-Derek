from unittest import TestCase
from connect_four.win_conditions.check_vertical_win import check_vertical_win


class TestCheckVerticalWin(TestCase):
    def test_check_vertical_win_type_error_board_not_dict(self):
        with self.assertRaises(TypeError):
            check_vertical_win(board=True, chosen_column=1, rows=1)

    def test_check_vertical_win_type_error_chosen_column_not_int(self):
        with self.assertRaises(TypeError):
            check_vertical_win(board={}, chosen_column="1", rows=1)

    def test_check_vertical_win_type_error_rows_not_int(self):
        with self.assertRaises(TypeError):
            check_vertical_win(board={}, chosen_column=1, rows="1")

    def test_check_vertical_win_value_error_rows_negative(self):
        with self.assertRaises(ValueError):
            check_vertical_win(board={}, chosen_column=1, rows=-100)

    def test_check_vertical_win_not_enough_rows_on_board(self):
        test_board = {(1, 1): "[O]", (1, 2): "[ ]", (2, 1): "[O]", (2, 2): "[ ]", (3, 1): "[O]", (3, 2): "[ ]"}
        self.assertFalse(check_vertical_win(board=test_board, chosen_column=1, rows=3))

    def test_check_vertical_win_standard_win(self):
        test_board = {(1, 1): '[O]', (1, 2): '[ ]', (2, 1): '[O]', (2, 2): '[ ]', (3, 1): '[O]',
                      (3, 2): '[ ]', (4, 1): '[O]', (4, 2): '[ ]'}
        self.assertTrue(check_vertical_win(board=test_board, chosen_column=1, rows=4))

    def test_check_vertical_win_standard_not_win(self):
        test_board = {(1, 1): '[O]', (1, 2): '[ ]', (2, 1): '[O]', (2, 2): '[ ]', (3, 1): '[O]',
                      (3, 2): '[O]', (4, 1): '[O]', (4, 2): '[O]'}
        self.assertFalse(check_vertical_win(board=test_board, chosen_column=2, rows=4))

    def test_check_vertical_win_column_all_blanks(self):
        test_board = {(1, 1): '[ ]', (1, 2): '[ ]', (2, 1): '[ ]', (2, 2): '[ ]', (3, 1): '[ ]',
                      (3, 2): '[O]', (4, 1): '[ ]', (4, 2): '[O]'}
        self.assertFalse(check_vertical_win(board=test_board, chosen_column=1, rows=4))

    def test_check_vertical_win_at_least_four_rows_too_many_and_win(self):
        test_board = {(1, 1): '[ ]', (1, 2): '[O]', (2, 1): '[ ]', (2, 2): '[O]', (3, 1): '[ ]',
                      (3, 2): '[O]', (4, 1): '[ ]', (4, 2): '[O]'}
        self.assertTrue(check_vertical_win(board=test_board, chosen_column=2, rows=8))

    def test_check_vertical_win_at_least_four_rows_too_many_and_not_win(self):
        test_board = {(1, 1): '[ ]', (1, 2): '[O]', (2, 1): '[ ]', (2, 2): '[O]', (3, 1): '[ ]',
                      (3, 2): '[O]', (4, 1): '[O]', (4, 2): '[O]'}
        self.assertFalse(check_vertical_win(board=test_board, chosen_column=1, rows=8))
