from blackjack.sum_non_aces import sum_non_aces


def sum_aces(hand: list) -> int:
    """
    Sum values of aces in hand.

    :param hand: a list representing hand dealt to the player or the dealer
    :precondition: hand must be a list
    :precondition: hand must only contain dictionaries
    :precondition: each item in hand must have a key called value
    :precondition: the value for the key called value in each item must be an integer
    :postcondition: scales the value of each ace depending on hand
    :postcondition: sums the values of all aces in hand
    :return: the scaled sum of value of the aces in hand
    :raises TypeError: if hand is not a list
    :raises TypeError: if hand has an element that is not a dictionary
    :raises TypeError: if the value for the key called value in each element is not an integer
    >>> test_hand_no_aces = [{"name": "8", "value": 8},{"name": "King", "value": 10}]
    >>> sum_aces(test_hand_no_aces)
    0
    >>> test_hand_some_aces_mixed = [{"name": "Ace", "value": 1},
    ... {"name": "8", "value": 8}, {"name": "Ace", "value": 1}, {"name": "4", "value": 4}]
    >>> sum_aces(test_hand_some_aces_mixed)
    2
    >>> test_hand_all_aces = [{"name": "Ace", "value": 1},{"name": "Ace", "value": 1}]
    >>> sum_aces(test_hand_all_aces)
    12
    """
    if type(hand) is not list:
        raise TypeError("The hand must be a list.")
    for card in hand:
        if type(card) is not dict:
            raise TypeError("Each card must be a dictionary.")
        if type(card.get("value")) is not int:
            raise TypeError("The value of the key called value in each card must exist and be an integer.")
    sum_of_aces = 0
    sum_of_non_aces = sum_non_aces(hand)
    count_of_aces = sum(card.get("value") == 1 for card in hand)
    for card in hand:
        if card.get("value") == 1:
            if sum_of_aces + sum_of_non_aces + 11 <= 21 - count_of_aces + 1:
                sum_of_aces += 11
            else:
                sum_of_aces += 1
    return sum_of_aces


def main():
    """
    Drive the program.
    """
    print("Welcome to the module")


if __name__ == "__main__":
    main()
