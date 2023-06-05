from unittest import TestCase
from connect_four.win_conditions.check_horizontal_win import check_horizontal_win


class TestCheckVerticalWin(TestCase):
    def test_check_horizontal_win_type_error_board_not_dict(self):
        with self.assertRaises(TypeError):
            check_horizontal_win(board=True, chosen_row=1, columns=1)

    def test_check_horizontal_win_type_error_chosen_row_not_int(self):
        with self.assertRaises(TypeError):
            check_horizontal_win(board={}, chosen_row="1", columns=1)

    def test_check_horizontal_win_type_error_columns_not_int(self):
        with self.assertRaises(TypeError):
            check_horizontal_win(board={}, chosen_row=1, columns="1")

    def test_check_horizontal_win_value_error_columns_negative(self):
        with self.assertRaises(ValueError):
            check_horizontal_win(board={}, chosen_row=1, columns=-100)

    def test_check_horizontal_win_not_enough_columns_on_board(self):
        test_board = {(1, 1): "[O]", (1, 2): "[ ]", (2, 1): "[O]", (2, 2): "[ ]", (3, 1): "[O]", (3, 2): "[ ]"}
        self.assertFalse(check_horizontal_win(board=test_board, chosen_row=1, columns=3))

    def test_check_horizontal_win_standard_win(self):
        test_board = {(1, 1): '[O]', (1, 2): '[ ]', (1, 3): '[O]', (1, 4): '[ ]', (2, 1): '[O]',
                      (2, 2): '[O]', (2, 3): '[O]', (2, 4): '[O]'}
        self.assertTrue(check_horizontal_win(board=test_board, chosen_row=2, columns=4))

    def test_check_horizontal_win_standard_not_win(self):
        test_board = {(1, 1): '[O]', (1, 2): '[ ]', (1, 3): '[O]', (1, 4): '[ ]', (2, 1): '[O]',
                      (2, 2): '[O]', (2, 3): '[O]', (2, 4): '[O]'}
        self.assertFalse(check_horizontal_win(board=test_board, chosen_row=1, columns=4))

    def test_check_horizontal_win_row_all_blanks(self):
        test_board = {(1, 1): '[ ]', (1, 2): '[ ]', (1, 3): '[ ]', (1, 4): '[ ]', (2, 1): '[O]',
                      (2, 2): '[O]', (2, 3): '[O]', (2, 4): '[O]'}
        self.assertFalse(check_horizontal_win(board=test_board, chosen_row=1, columns=4))

    def test_check_horizontal_win_at_least_four_columns_too_many_and_win(self):
        test_board = {(1, 1): '[O]', (1, 2): '[ ]', (1, 3): '[O]', (1, 4): '[ ]', (2, 1): '[O]',
                      (2, 2): '[O]', (2, 3): '[O]', (2, 4): '[O]'}
        self.assertTrue(check_horizontal_win(board=test_board, chosen_row=2, columns=8))

    def test_check_horizontal_win_at_least_four_columns_too_many_and_not_win(self):
        test_board = {(1, 1): '[ ]', (1, 2): '[ ]', (1, 3): '[ ]', (1, 4): '[ ]', (2, 1): '[O]',
                      (2, 2): '[O]', (2, 3): '[O]', (2, 4): '[O]'}
        self.assertFalse(check_horizontal_win(board=test_board, chosen_row=1, columns=8))

    def test_check_horizontal_win_board_empty_dict(self):
        self.assertFalse(check_horizontal_win(board={}, chosen_row=4, columns=4))
