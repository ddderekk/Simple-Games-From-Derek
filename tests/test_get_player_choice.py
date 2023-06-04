import io
from unittest import TestCase
from common_features.get_player_choice import get_player_choice
from unittest.mock import patch


class TestGetPlayerChoice(TestCase):
    def test_get_player_choice_type_error_valid_inputs_not_tuple(self):
        with self.assertRaises(TypeError):
            get_player_choice(True, "hello")

    def test_get_player_choice_type_error_prompt_not_string(self):
        with self.assertRaises(TypeError):
            get_player_choice(("1", "2"), True)

    def test_get_player_choice_type_error_valid_inputs_not_all_strings(self):
        with self.assertRaises(TypeError):
            get_player_choice(("1", 2), "Hehe")

    @patch("builtins.input", side_effect=["1"])
    def test_get_player_choice_valid_choice_first(self, _):
        expected_result = "1"
        actual_result = get_player_choice(valid_inputs=("1", "2", "3"), prompt="Choose 1, 2, or 3")
        self.assertEqual(expected_result, actual_result)

    @patch("builtins.input", side_effect=["One", "1"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_player_choice_valid_choice_second(self, mock_output, _):
        expected_result = "1"
        actual_result = get_player_choice(valid_inputs=("1", "2", "3"), prompt="Choose 1, 2, or 3")
        expected_output = "You can't do that."
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_result, actual_result)
        self.assertIn(expected_output, actual_output)
