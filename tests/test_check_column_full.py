from unittest import TestCase
from connect_four.player_choice.check_column_full import check_column_full


class TestCheckColumnFull(TestCase):
    def test_check_column_full_type_error_board_not_dict(self):
        with self.assertRaises(TypeError):
            check_column_full(board=True, chosen_column=1, rows=1)

    def test_check_column_full_type_error_column_not_int(self):
        with self.assertRaises(TypeError):
            check_column_full(board={}, chosen_column="1", rows=1)

    def test_check_column_full_type_error_rows_not_int(self):
        with self.assertRaises(TypeError):
            check_column_full(board={}, chosen_column=5, rows="5")

    def test_check_column_full_value_error_rows_negative(self):
        with self.assertRaises(ValueError):
            check_column_full(board={}, chosen_column=5, rows=-5)

    def test_check_column_full_column_not_in_board(self):
        test_board = {(1, 1): "[ ]", (1, 2): "[ ]", (2, 1): "[ ]", (2, 2): "[ ]"}
        self.assertTrue(check_column_full(test_board, chosen_column=3, rows=2))

    def test_check_column_full_too_many_rows_full_column(self):
        test_board = {(1, 1): "[O]", (1, 2): "[ ]", (2, 1): "[O]", (2, 2): "[ ]"}
        self.assertTrue(check_column_full(test_board, chosen_column=1, rows=5))

    def test_check_column_full_board_full(self):
        test_board = {(1, 1): "[O]", (1, 2): "[O]", (2, 1): "[O]", (2, 2): "[O]"}
        self.assertTrue(check_column_full(test_board, chosen_column=2, rows=2))

    def test_check_column_full_board_empty(self):
        test_board = {(1, 1): "[ ]", (1, 2): "[ ]", (2, 1): "[ ]", (2, 2): "[ ]"}
        self.assertFalse(check_column_full(test_board, chosen_column=2, rows=2))

    def test_check_column_full_column_full_but_not_chosen(self):
        test_board = {(1, 1): "[0]", (1, 2): "[ ]", (2, 1): "[0]", (2, 2): "[ ]"}
        self.assertFalse(check_column_full(test_board, chosen_column=2, rows=2))

    def test_check_column_full_column_full_and_chosen(self):
        test_board = {(1, 1): "[0]", (1, 2): "[ ]", (2, 1): "[0]", (2, 2): "[ ]"}
        self.assertTrue(check_column_full(test_board, chosen_column=1, rows=2))

    def test_check_column_full_board_empty_dict(self):
        self.assertTrue(check_column_full(board={}, chosen_column=1, rows=2))
