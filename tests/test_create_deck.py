from unittest import TestCase
from blackjack.create_deck import create_deck


class TestCreateDeck(TestCase):
    def test_create_deck(self):
        expected_result = [{'name': 'Ace', 'suite': 'Spades', 'value': 1},
                           {'name': 'Ace', 'suite': 'Clubs', 'value': 1},
                           {'name': 'Ace', 'suite': 'Diamonds', 'value': 1},
                           {'name': 'Ace', 'suite': 'Hearts', 'value': 1},
                           {'name': '2', 'suite': 'Spades', 'value': 2}, {'name': '2', 'suite': 'Clubs', 'value': 2},
                           {'name': '2', 'suite': 'Diamonds', 'value': 2}, {'name': '2', 'suite': 'Hearts', 'value': 2},
                           {'name': '3', 'suite': 'Spades', 'value': 3}, {'name': '3', 'suite': 'Clubs', 'value': 3},
                           {'name': '3', 'suite': 'Diamonds', 'value': 3}, {'name': '3', 'suite': 'Hearts', 'value': 3},
                           {'name': '4', 'suite': 'Spades', 'value': 4}, {'name': '4', 'suite': 'Clubs', 'value': 4},
                           {'name': '4', 'suite': 'Diamonds', 'value': 4}, {'name': '4', 'suite': 'Hearts', 'value': 4},
                           {'name': '5', 'suite': 'Spades', 'value': 5}, {'name': '5', 'suite': 'Clubs', 'value': 5},
                           {'name': '5', 'suite': 'Diamonds', 'value': 5}, {'name': '5', 'suite': 'Hearts', 'value': 5},
                           {'name': '6', 'suite': 'Spades', 'value': 6}, {'name': '6', 'suite': 'Clubs', 'value': 6},
                           {'name': '6', 'suite': 'Diamonds', 'value': 6}, {'name': '6', 'suite': 'Hearts', 'value': 6},
                           {'name': '7', 'suite': 'Spades', 'value': 7}, {'name': '7', 'suite': 'Clubs', 'value': 7},
                           {'name': '7', 'suite': 'Diamonds', 'value': 7}, {'name': '7', 'suite': 'Hearts', 'value': 7},
                           {'name': '8', 'suite': 'Spades', 'value': 8}, {'name': '8', 'suite': 'Clubs', 'value': 8},
                           {'name': '8', 'suite': 'Diamonds', 'value': 8}, {'name': '8', 'suite': 'Hearts', 'value': 8},
                           {'name': '9', 'suite': 'Spades', 'value': 9}, {'name': '9', 'suite': 'Clubs', 'value': 9},
                           {'name': '9', 'suite': 'Diamonds', 'value': 9}, {'name': '9', 'suite': 'Hearts', 'value': 9},
                           {'name': '10', 'suite': 'Spades', 'value': 10},
                           {'name': '10', 'suite': 'Clubs', 'value': 10},
                           {'name': '10', 'suite': 'Diamonds', 'value': 10},
                           {'name': '10', 'suite': 'Hearts', 'value': 10},
                           {'name': 'Jack', 'suite': 'Spades', 'value': 10},
                           {'name': 'Jack', 'suite': 'Clubs', 'value': 10},
                           {'name': 'Jack', 'suite': 'Diamonds', 'value': 10},
                           {'name': 'Jack', 'suite': 'Hearts', 'value': 10},
                           {'name': 'Queen', 'suite': 'Spades', 'value': 10},
                           {'name': 'Queen', 'suite': 'Clubs', 'value': 10},
                           {'name': 'Queen', 'suite': 'Diamonds', 'value': 10},
                           {'name': 'Queen', 'suite': 'Hearts', 'value': 10},
                           {'name': 'King', 'suite': 'Spades', 'value': 10},
                           {'name': 'King', 'suite': 'Clubs', 'value': 10},
                           {'name': 'King', 'suite': 'Diamonds', 'value': 10},
                           {'name': 'King', 'suite': 'Hearts', 'value': 10}]
        actual_result = create_deck()
        self.assertEqual(expected_result, actual_result)
