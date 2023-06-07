def sum_non_aces(hand: list) -> int:
    """
    Sum values of all cards in hand that are not Aces.

    :param hand: a list representing hand dealt to the player or the dealer
    :precondition: hand must be a list
    :precondition: hand must only contain dictionaries
    :precondition: each item in hand must have a key called value
    :precondition: the value for the key called value in each item must be an integer
    :postcondition: sums the values of the key called value from all elements in hand
    :return: the sum of the values for the key called value from all elements in hand as an integer
    :raises TypeError: if hand is not a list
    :raises TypeError: if hand has an element that is not a dictionary
    :raises TypeError: if the value for the key called value in each element is not an integer
    >>> test_hand_no_aces = [{"name": "8", "value": 8},{"name": "King", "value": 10}]
    >>> sum_non_aces(test_hand_no_aces)
    18
    >>> test_hand_some_aces_mixed = [{"name": "Ace", "value": 1},
    ... {"name": "8", "value": 8}, {"name": "Ace", "value": 1}, {"name": "4", "value": 4}]
    >>> sum_non_aces(test_hand_some_aces_mixed)
    12
    >>> test_hand_all_aces = [{"name": "Ace", "value": 1},{"name": "Ace", "value": 1}]
    >>> sum_non_aces(test_hand_all_aces)
    0
    """
    if type(hand) is not list:
        raise TypeError("The hand must be a list.")
    for card in hand:
        if type(card) is not dict:
            raise TypeError("Each card must be a dictionary.")
        if type(card.get("value")) is not int:
            raise TypeError("The value of the key called value in each card must exist and be an integer.")
    sum_of_non_aces = 0
    for card in hand:
        if card.get("value") != 1 and card.get("value") is not None:
            sum_of_non_aces += card.get("value")
    return sum_of_non_aces


def main():
    """
    Drive the program.
    """
    print("Welcome to the module")


if __name__ == "__main__":
    main()
