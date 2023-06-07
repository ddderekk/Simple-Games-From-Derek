from unittest import TestCase
from blackjack.sum_non_aces import sum_non_aces


class TestSumNonAces(TestCase):
    def test_sum_non_aces_type_error_hand_not_list(self):
        with self.assertRaises(TypeError):
            sum_non_aces(hand={})

    def test_sum_non_aces_type_error_hand_has_non_dict_items(self):
        with self.assertRaises(TypeError):
            sum_non_aces(hand=[(), ()])

    def test_sum_non_aces_type_error_value_in_card_not_int(self):
        with self.assertRaises(TypeError):
            sum_non_aces(hand=[{"value": True}, {"value": 1}])

    def test_sum_non_aces_type_error_no_value_key_in_card(self):
        with self.assertRaises(TypeError):
            sum_non_aces(hand=[{}, {"value": 1}])

    def test_sum_non_aces_no_aces(self):
        test_hand_no_aces = [{"name": "8", "value": 8}, {"name": "King", "value": 10}]
        self.assertEqual(18, sum_non_aces(hand=test_hand_no_aces))

    def test_sum_non_aces_all_aces(self):
        test_hand_all_aces = [{"name": "Ace", "value": 1}, {"name": "Ace", "value": 1}]
        self.assertEqual(0, sum_non_aces(hand=test_hand_all_aces))

    def test_sum_non_aces_mix_aces(self):
        test_hand_some_aces_mixed = [{"name": "Ace", "value": 1}, {"name": "8", "value": 8},
                                     {"name": "Ace", "value": 1}, {"name": "4", "value": 4}, {"name": "2", "value": 2}]
        self.assertEqual(14, sum_non_aces(hand=test_hand_some_aces_mixed))

    def test_sum_non_aces_empty_hand(self):
        self.assertEqual(0, sum_non_aces(hand=[]))

    def test_sum_non_aces_called_ace_but_values_are_not_one(self):
        test_hand_wrong_value_for_ace = [{"name": "Ace", "value": 2}, {"name": "8", "value": 8}]
        self.assertEqual(10, sum_non_aces(hand=test_hand_wrong_value_for_ace))

    def test_sum_non_aces_values_are_one_but_name_not_ace(self):
        test_hand_wrong_name_for_value_one = [{"name": "2", "value": 2}, {"name": "8", "value": 1}]
        self.assertEqual(2, sum_non_aces(hand=test_hand_wrong_name_for_value_one))
