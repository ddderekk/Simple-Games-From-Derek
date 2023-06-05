from unittest import TestCase
from connect_four.show_player.show_column_headers import show_column_headers
from unittest.mock import patch
import io


class TestShowColumnHeaders(TestCase):
    def test_show_column_headers_type_error_columns_not_int(self):
        with self.assertRaises(TypeError):
            show_column_headers("5")

    def test_show_column_headers_value_error_columns_negative(self):
        with self.assertRaises(ValueError):
            show_column_headers(-5)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_column_headers_zero(self, mock_output):
        show_column_headers(0)
        expected_output = ""
        actual_output = mock_output.getvalue()
        self.assertIn(expected_output, actual_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_column_headers_one(self, mock_output):
        show_column_headers(1)
        expected_output = " 1 "
        actual_output = mock_output.getvalue()
        self.assertIn(expected_output, actual_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_column_headers_three(self, mock_output):
        show_column_headers(3)
        expected_output = " 1   2   3 "
        actual_output = mock_output.getvalue()
        self.assertIn(expected_output, actual_output)
