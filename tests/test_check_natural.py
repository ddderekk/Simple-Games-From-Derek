from unittest import TestCase
from blackjack.check_natural import check_natural


class TestCheckNatural(TestCase):
    def test_check_natural_type_error_hand_not_list(self):
        with self.assertRaises(TypeError):
            check_natural(hand=())

    def test_check_natural_type_error_hand_not_only_dicts(self):
        with self.assertRaises(TypeError):
            check_natural(hand=[{}, {1}])

    def test_check_natural_type_error_hand_not_two_cards(self):
        with self.assertRaises(ValueError):
            check_natural(hand=[{}])

    def test_check_natural_ace_of_spades_natural(self):
        test_hand = [{"name": "Ace", "suite": "Spades", "value": 1}, {"name": "10", "suite": "Spades", "value": 10}]
        self.assertTrue(check_natural(hand=test_hand))

    def test_check_natural_ace_of_clubs_natural(self):
        test_hand = [{"name": "Ace", "suite": "Clubs", "value": 1}, {"name": "10", "suite": "Spades", "value": 10}]
        self.assertTrue(check_natural(hand=test_hand))

    def test_check_natural_ace_of_diamonds_natural(self):
        test_hand = [{"name": "Ace", "suite": "Diamonds", "value": 1}, {"name": "10", "suite": "Spades", "value": 10}]
        self.assertTrue(check_natural(hand=test_hand))

    def test_check_natural_ace_of_hearts_natural(self):
        test_hand = [{"name": "Ace", "suite": "Hearts", "value": 1}, {"name": "10", "suite": "Spades", "value": 10}]
        self.assertTrue(check_natural(hand=test_hand))

    def test_check_natural_natural_reverse_ordered(self):
        test_hand = [{"name": "10", "suite": "Spades", "value": 10}, {"name": "Ace", "suite": "Hearts", "value": 1}]
        self.assertTrue(check_natural(hand=test_hand))

    def test_check_natural_natural_with_jack(self):
        test_hand = [{"name": "Ace", "suite": "Hearts", "value": 1}, {"name": "Jack", "suite": "Spades", "value": 10}]
        self.assertTrue(check_natural(hand=test_hand))

    def test_check_natural_natural_with_queen(self):
        test_hand = [{"name": "Ace", "suite": "Hearts", "value": 1}, {"name": "Queen", "suite": "Spades", "value": 10}]
        self.assertTrue(check_natural(hand=test_hand))

    def test_check_natural_natural_with_king(self):
        test_hand = [{"name": "Ace", "suite": "Hearts", "value": 1}, {"name": "King", "suite": "Spades", "value": 10}]
        self.assertTrue(check_natural(hand=test_hand))

    def test_check_natural_not_natural_ace_and_not_ten(self):
        test_hand = [{"name": "Ace", "suite": "Hearts", "value": 1}, {"name": "7", "suite": "Spades", "value": 7}]
        self.assertFalse(check_natural(hand=test_hand))

    def test_check_natural_not_natural_ten_and_not_ace(self):
        test_hand = [{"name": "10", "suite": "Hearts", "value": 10}, {"name": "7", "suite": "Spades", "value": 7}]
        self.assertFalse(check_natural(hand=test_hand))

    def test_check_natural_two_aces(self):
        test_hand = [{"name": "Ace", "suite": "Hearts", "value": 11}, {"name": "Ace", "suite": "Spades", "value": 11}]
        self.assertFalse(check_natural(hand=test_hand))

    def test_check_natural_two_tens(self):
        test_hand = [{"name": "10", "suite": "Spades", "value": 10}, {"name": "10", "suite": "Hearts", "value": 10}]
        self.assertFalse(check_natural(hand=test_hand))
