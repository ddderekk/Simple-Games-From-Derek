from unittest import TestCase
from blackjack.place_wager import place_wager
from unittest.mock import patch
import io


class TestPlaceWager(TestCase):
    def test_place_wager_type_error_limit_not_int(self):
        with self.assertRaises(TypeError):
            place_wager("500")

    def test_place_wager_value_error_limit_zero(self):
        with self.assertRaises(ValueError):
            place_wager(0)

    def test_place_wager_value_error_limit_negative(self):
        with self.assertRaises(ValueError):
            place_wager(-1)

    @patch('builtins.input', side_effect=["100"])
    def test_place_wager_first_choice_within_limit(self, _):
        expected_result = 100
        actual_result = place_wager(limit=500)
        self.assertEqual(expected_result, actual_result)

    @patch('builtins.input', side_effect=["500"])
    def test_place_wager_first_choice_on_limit(self, _):
        expected_result = 500
        actual_result = place_wager(limit=500)
        self.assertEqual(expected_result, actual_result)

    @patch('builtins.input', side_effect=["Hundred", "100"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_place_wager_word_first_then_number(self, mock_output, _):
        expected_result = 100
        actual_result = place_wager(limit=500)
        expected_output = "You can't do that.\n"
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
        self.assertEqual(expected_result, actual_result)

    @patch('builtins.input', side_effect=["600", "100"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_place_wager_number_not_in_limit_first_then_in_limit(self, mock_output, _):
        expected_result = 100
        actual_result = place_wager(limit=500)
        expected_output = "You can't do that.\n"
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
        self.assertEqual(expected_result, actual_result)

    @patch('builtins.input', side_effect=["-100", "100"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_place_wager_negative_wager_first_then_positive_in_limit(self, mock_output, _):
        expected_result = 100
        actual_result = place_wager(limit=500)
        expected_output = "You can't do that.\n"
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
        self.assertEqual(expected_result, actual_result)

    @patch('builtins.input', side_effect=["100.0", "100"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_place_wager_decimal_wager_first_then_integer_in_limit(self, mock_output, _):
        expected_result = 100
        actual_result = place_wager(limit=500)
        expected_output = "You can't do that.\n"
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
        self.assertEqual(expected_result, actual_result)

    @patch('builtins.input', side_effect=["Hundred", "100.0", "-100", "1000", "100"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_place_wager_word_decimal_negative_over_limit(self, mock_output, _):
        expected_result = 100
        actual_result = place_wager(limit=500)
        expected_output = "You can't do that.\nYou can't do that.\nYou can't do that.\nYou can't do that.\n"
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
        self.assertEqual(expected_result, actual_result)
