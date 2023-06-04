from unittest import TestCase
from common_features.check_board_full import check_board_full


class TestCheckBoardFull(TestCase):
    def test_check_board_full_type_error_board_not_dict(self):
        with self.assertRaises(TypeError):
            check_board_full((1, 2), "[ ]")

    def test_check_board_full_type_error_blank_space_not_string(self):
        with self.assertRaises(TypeError):
            check_board_full({}, [])

    def test_check_board_empty_board(self):
        self.assertTrue(check_board_full({}, "[ ]"))

    def test_check_board_full_board_is_full(self):
        self.assertTrue(check_board_full({(1, 1): "[\033[31mO\033[37m]", (1, 2): "[\033[31mO\033[37m]"},  "[ ]"))

    def test_check_board_full_board_is_not_full(self):
        self.assertFalse(check_board_full({(1, 1): "[\033[31mO\033[37m]", (1, 2): "[ ]"},  "[ ]"))
