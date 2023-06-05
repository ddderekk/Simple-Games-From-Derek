from unittest import TestCase
from connect_four.player_choice.find_open_space import find_open_space


class TestFindOpenSpace(TestCase):
    def test_find_open_space_type_error_board_not_dict(self):
        with self.assertRaises(TypeError):
            find_open_space(True, 1, 1)

    def test_find_open_space_type_error_chosen_column_not_int(self):
        with self.assertRaises(TypeError):
            find_open_space({}, "1", 1)

    def test_find_open_space_type_error_rows_not_int(self):
        with self.assertRaises(TypeError):
            find_open_space({}, 1, "1")

    def test_find_open_space_value_error_rows_negative(self):
        with self.assertRaises(ValueError):
            find_open_space({}, 1, -1)

    def test_find_open_space_open_bottom(self):
        test_board_open_at_bottom = {(1, 1): '[O]', (1, 2): '[ ]', (2, 1): '[O]', (2, 2): '[ ]'}
        expected_result = (2, 2)
        actual_result = find_open_space(board=test_board_open_at_bottom, chosen_column=2, rows=2)
        self.assertEqual(expected_result, actual_result)

    def test_find_open_space_open_middle(self):
        test_board_open_middle = {(1, 1): '[ ]', (1, 2): '[O]', (1, 3): '[ ]', (2, 1): '[O]', (2, 2): '[O]',
                                  (2, 3): '[ ]', (3, 1): '[ ]', (3, 2): '[O]', (3, 3): '[O]'}
        expected_result = (2, 3)
        actual_result = find_open_space(board=test_board_open_middle, chosen_column=3, rows=3)
        self.assertEqual(expected_result, actual_result)

    def test_find_open_space_open_top(self):
        test_board_open_top = {(1, 1): '[ ]', (1, 2): '[ ]', (1, 3): '[ ]', (2, 1): '[O]', (2, 2): '[O]',
                               (2, 3): '[ ]', (3, 1): '[ ]', (3, 2): '[O]', (3, 3): '[O]'}
        expected_result = (1, 2)
        actual_result = find_open_space(board=test_board_open_top, chosen_column=2, rows=3)
        self.assertEqual(expected_result, actual_result)

    def test_find_open_space_full_board(self):
        test_board_full = {(1, 1): '[O]', (1, 2): '[O]', (2, 1): '[O]', (2, 2): '[O]'}
        expected_result = ()
        actual_result = find_open_space(board=test_board_full, chosen_column=1, rows=2)
        self.assertEqual(expected_result, actual_result)

    def test_find_open_space_too_many_rows(self):
        test_board_full = {(1, 1): '[ ]', (1, 2): '[O]', (2, 1): '[O]', (2, 2): '[O]'}
        expected_result = (1, 1)
        actual_result = find_open_space(board=test_board_full, chosen_column=1, rows=5)
        self.assertEqual(expected_result, actual_result)
