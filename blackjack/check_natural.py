def check_natural(hand: list) -> bool:
    """
    Check if the hand has both an ace and a 10 valued card and nothing else.

    :param hand: a list representing the 2 card hand dealt to the player or the dealer
    :precondition: hand must be a list
    :precondition: hand must only contain dictionaries
    :precondition: the length of hand must be 2
    :precondition: each item in hand must have a key called name
    :precondition: each item in hand must have a key called value
    :postcondition: checks if hand has a dictionary with the name Ace and a dictionary with the value 10
    :return: True if hand has a dictionary with the name Ace and a dictionary with the value 10, else False
    :raises TypeError: if hand is not a list
    :raises ValueError: if the length of hand is not 2
    :raises TypeError: if hand has an element that is not a dictionary
    >>> test_hand_natural = [{"name": "Ace", "value": 11}, {"name": "10", "value": 10}]
    >>> check_natural(test_hand_natural)
    True
    >>> test_hand_natural_with_face_card = [{"name": "King", "value": 10}, {"name": "Ace", "value": 11}]
    >>> check_natural(test_hand_natural_with_face_card)
    True
    >>> test_hand_not_natural = [{"name": "9", "value": 9}, {"name": "Ace", "value": 11}]
    >>> check_natural(test_hand_not_natural)
    False
    """
    if type(hand) is not list:
        raise TypeError("The hand must be a list.")
    for card in hand:
        if type(card) is not dict:
            raise TypeError("Each card must be a dictionary.")
    if len(hand) != 2:
        raise ValueError("Your hand must only have 2 cards in it.")

    if hand[0].get("name") == "Ace" and hand[1].get("value") == 10 or \
            hand[1].get("name") == "Ace" and hand[0].get("value") == 10:
        return True
    return False


def main():
    """
    Drive the program.
    """
    print("Welcome to the module")


if __name__ == "__main__":
    main()
