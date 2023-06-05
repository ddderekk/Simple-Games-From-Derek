from unittest import TestCase
from common_features.show_board import show_board
from unittest.mock import patch
import io


class TestShowBoard(TestCase):
    def test_show_board_type_error_board_not_dict(self):
        with self.assertRaises(TypeError):
            show_board(board="{}", rows=5, columns=5)

    def test_show_board_type_error_rows_not_int(self):
        with self.assertRaises(TypeError):
            show_board(board={}, rows="5", columns=5)

    def test_show_board_type_error_columns_not_int(self):
        with self.assertRaises(TypeError):
            show_board(board={}, rows=5, columns="5")

    def test_show_board_value_error_rows_negative(self):
        with self.assertRaises(ValueError):
            show_board(board={}, rows=-5, columns=5)

    def test_show_board_value_error_columns_negative(self):
        with self.assertRaises(ValueError):
            show_board(board={}, rows=5, columns=-5)

    def test_show_board_type_error_and_value_error_combined(self):
        with self.assertRaises(TypeError):
            show_board(board="{}", rows=-5, columns=-5)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_board_empty_board(self, mock_output):
        test_board_square = {}
        show_board(board=test_board_square, rows=2, columns=2)
        expected_output = "None None \nNone None \n"
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_board_no_rows(self, mock_output):
        test_board_square = {(1, 1): "[ ]", (1, 2): "[O]", (2, 1): "[ ]", (2, 2): "[O]"}
        show_board(board=test_board_square, rows=0, columns=2)
        expected_output = ""
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_board_no_columns_has_rows(self, mock_output):
        test_board_square = {(1, 1): "[ ]", (1, 2): "[O]", (2, 1): "[ ]", (2, 2): "[O]"}
        show_board(board=test_board_square, rows=2, columns=0)
        expected_output = "\n\n"
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_board_no_columns_no_rows(self, mock_output):
        test_board_square = {(1, 1): "[ ]", (1, 2): "[O]", (2, 1): "[ ]", (2, 2): "[O]"}
        show_board(board=test_board_square, rows=0, columns=0)
        expected_output = ""
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_board_no_columns_ones(self, mock_output):
        test_board_square = {(1, 1): "[ ]", (1, 2): "[O]", (2, 1): "[ ]", (2, 2): "[O]"}
        show_board(board=test_board_square, rows=1, columns=1)
        expected_output = "[ ] \n"
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_board_square(self, mock_output):
        test_board_square = {(1, 1): "[ ]", (1, 2): "[O]", (2, 1): "[ ]", (2, 2): "[O]"}
        show_board(board=test_board_square, rows=2, columns=2)
        expected_output = "[ ] [O] \n[ ] [O]"
        actual_output = mock_output.getvalue()
        self.assertIn(expected_output, actual_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_board_wide_rectangle(self, mock_output):
        test_board_wide_rectangle = {(1, 1): "[ ]", (1, 2): "[O]", (1, 3): "[ ]", (1, 4): "[O]",
                                     (2, 1): "[ ]", (2, 2): "[O]", (2, 3): "[ ]", (2, 4): "[O]"}
        show_board(board=test_board_wide_rectangle, rows=2, columns=4)
        expected_output = "[ ] [O] [ ] [O] \n[ ] [O] [ ] [O] \n"
        actual_output = mock_output.getvalue()
        self.assertIn(expected_output, actual_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_board_long_rectangle(self, mock_output):
        test_board_long_rectangle = {(1, 1): "[O]", (1, 2): "[O]", (1, 3): "[O]", (2, 1): "[O]",
                                     (2, 2): "[O]", (2, 3): "[O]", (3, 1): "[O]", (3, 2): "[O]", (3, 3): "[O]",
                                     (4, 1): "[O]", (4, 2): "[O]", (4, 3): "[O]"}
        show_board(board=test_board_long_rectangle, rows=4, columns=3)
        expected_output = "[O] [O] [O] \n[O] [O] [O] \n[O] [O] [O] \n[O] [O] [O] \n"
        actual_output = mock_output.getvalue()
        self.assertIn(expected_output, actual_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_board_too_many_rows(self, mock_output):
        test_board = {(1, 1): "[O]", (1, 2): "[O]", (2, 1): "[O]", (2, 2): "[ ]"}
        show_board(board=test_board, rows=7, columns=2)
        expected_output = "[O] [O] \n[O] [ ] \n"
        actual_output = mock_output.getvalue()
        self.assertIn(expected_output, actual_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_board_too_many_columns(self, mock_output):
        test_board = {(1, 1): "[O]", (1, 2): "[O]", (2, 1): "[O]", (2, 2): "[ ]"}
        show_board(board=test_board, rows=2, columns=4)
        expected_output = "[O] [O] None None \n[O] [ ] None None \n"
        actual_output = mock_output.getvalue()
        self.assertIn(expected_output, actual_output)
