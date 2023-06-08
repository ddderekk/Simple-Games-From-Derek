from unittest import TestCase
from blackjack.sum_aces import sum_aces


class TestSumAces(TestCase):
    def test_sum_aces_type_error_hand_not_list(self):
        with self.assertRaises(TypeError):
            sum_aces(hand="[]")

    def test_sum_aces_type_error_cards_not_dict(self):
        with self.assertRaises(TypeError):
            sum_aces(hand=[[], []])

    def test_sum_aces_type_error_card_values_not_ints(self):
        with self.assertRaises(TypeError):
            sum_aces(hand=[{"value": "5"}, {"value": 5}])

    def test_sum_aces_four_aces(self):
        test_hand = [{"value": 1}, {"value": 1}, {"value": 1}, {"value": 1}]
        self.assertEqual(14, sum_aces(hand=test_hand))

    def test_sum_aces_four_aces_seventeen_non_ace_sum(self):
        test_hand = [{"value": 1}, {"value": 1}, {"value": 1}, {"value": 1}, {"value": 17}]
        self.assertEqual(4, sum_aces(hand=test_hand))

    def test_sum_aces_three_aces(self):
        test_hand = [{"value": 1}, {"value": 1}, {"value": 1}]
        self.assertEqual(13, sum_aces(hand=test_hand))

    def test_sum_aces_three_aces_eighteen_non_ace_sum(self):
        test_hand = [{"value": 1}, {"value": 1}, {"value": 1}, {"value": 10}, {"value": 8}]
        self.assertEqual(3, sum_aces(hand=test_hand))

    def test_sum_aces_two_aces(self):
        test_hand = [{"value": 1}, {"value": 1}]
        self.assertEqual(12, sum_aces(hand=test_hand))

    def test_sum_aces_two_aces_nineteen_non_ace_sum(self):
        test_hand = [{"value": 1}, {"value": 1}, {"value": 10}, {"value": 9}]
        self.assertEqual(2, sum_aces(hand=test_hand))

    def test_sum_aces_one_ace(self):
        test_hand = [{"value": 1}]
        self.assertEqual(11, sum_aces(hand=test_hand))

    def test_sum_aces_one_ace_twenty_non_ace_sum(self):
        test_hand = [{"value": 1}, {"value": 10}, {"value": 10}]
        self.assertEqual(1, sum_aces(hand=test_hand))

    def test_sum_aces_natural_blackjack(self):
        test_hand = [{"value": 10}, {"value": 1}]
        self.assertEqual(11, sum_aces(hand=test_hand))

    def test_sum_aces_no_aces(self):
        test_hand = [{"value": 5}, {"value": 5}]
        self.assertEqual(0, sum_aces(hand=test_hand))

    def test_sum_aces_mix_aces_and_others_over_twenty_one(self):
        test_hand = [{"value": 5}, {"value": 1}, {"value": 1}, {"value": 8}, {"value": 2}, {"value": 5}]
        self.assertEqual(2, sum_aces(hand=test_hand))
