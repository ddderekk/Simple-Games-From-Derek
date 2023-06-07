from unittest import TestCase
from blackjack.show_hand import show_hand


class TestShowHand(TestCase):
    def test_show_hand_type_error_hand_not_list(self):
        with self.assertRaises(TypeError):
            show_hand(hand={})

    def test_show_hand_type_error_hand_contains_non_dict(self):
        with self.assertRaises(TypeError):
            show_hand(hand=[()])

    def test_show_hand_empty_hand(self):
        self.assertEqual([], show_hand(hand=[]))

    def test_show_hand_one_card(self):
        test_hand = [{"name": "Ace", "suite": "Clubs"}]
        expected_result = ["Ace of Clubs"]
        self.assertEqual(expected_result, show_hand(hand=test_hand))

    def test_show_hand_multiple_cards(self):
        test_hand = [{"name": "Ace", "suite": "Clubs"}, {"name": "8", "suite": "Spades"},
                     {"name": "King", "suite": "Hearts"}]
        expected_result = ["Ace of Clubs", "8 of Spades", "King of Hearts"]
        self.assertEqual(expected_result, show_hand(hand=test_hand))

    def test_show_hand_no_name_in_card(self):
        test_hand = [{"suite": "Clubs"}]
        expected_result = ["None of Clubs"]
        self.assertEqual(expected_result, show_hand(hand=test_hand))

    def test_show_hand_no_suite_in_card(self):
        test_hand = [{"name": "Ace"}]
        expected_result = ["Ace of None"]
        self.assertEqual(expected_result, show_hand(hand=test_hand))

    def test_show_hand_no_name_or_suite_in_card(self):
        test_hand = [{}]
        expected_result = ["None of None"]
        self.assertEqual(expected_result, show_hand(hand=test_hand))
