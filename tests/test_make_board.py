from unittest import TestCase
from common_features.make_board import make_board_numbered


class TestMakeBoardNumbered(TestCase):
    def test_make_board_numbered_type_error_rows(self):
        with self.assertRaises(TypeError):
            make_board_numbered(rows=True, columns=1)

    def test_make_board_numbered_type_error_columns(self):
        with self.assertRaises(TypeError):
            make_board_numbered(rows=1, columns=False)

    def test_make_board_numbered_value_error_rows(self):
        with self.assertRaises(ValueError):
            make_board_numbered(rows=-1, columns=5)

    def test_make_board_numbered_value_error_columns(self):
        with self.assertRaises(ValueError):
            make_board_numbered(rows=5, columns=-1)

    def test_make_board_numbered_zeroes(self):
        test_board = make_board_numbered(rows=0, columns=0)
        expected_board = {}
        self.assertEqual(test_board, expected_board)

    def test_make_board_numbered_square(self):
        test_board = make_board_numbered(rows=3, columns=3)
        expected_board = {(1, 1): '[ ]', (1, 2): '[ ]', (1, 3): '[ ]', (2, 1): '[ ]',  (2, 2): '[ ]',  (2, 3): '[ ]',
                          (3, 1): '[ ]',  (3, 2): '[ ]',  (3, 3): '[ ]'}
        self.assertEqual(test_board, expected_board)

    def test_make_board_numbered_long_rectangle(self):
        test_board = make_board_numbered(rows=3, columns=1)
        expected_board = {(1, 1): '[ ]', (2, 1): '[ ]', (3, 1): '[ ]'}
        self.assertEqual(test_board, expected_board)

    def test_make_board_numbered_wide_rectangle(self):
        test_board = make_board_numbered(rows=1, columns=3)
        expected_board = {(1, 1): '[ ]', (1, 2): '[ ]', (1, 3): '[ ]'}
        self.assertEqual(test_board, expected_board)
