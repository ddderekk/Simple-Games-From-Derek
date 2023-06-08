def create_deck() -> list:
    """
    Create a deck of cards not including jokers where face cards are not all 10.

    :postcondition: creates a deck of cards as a list not including jokers where face cards are not all 10
    :return: a list of dictionaries for each card in a deck not including jokers where face cards are not all 10
    >>> create_deck() # doctest: +NORMALIZE_WHITESPACE
    [{'name': 'Ace', 'suite': 'Spades', 'value': 1}, {'name': 'Ace', 'suite': 'Clubs', 'value': 1},
    {'name': 'Ace', 'suite': 'Diamonds', 'value': 1}, {'name': 'Ace', 'suite': 'Hearts', 'value': 1},
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
    {'name': '10', 'suite': 'Spades', 'value': 10}, {'name': '10', 'suite': 'Clubs', 'value': 10},
    {'name': '10', 'suite': 'Diamonds', 'value': 10}, {'name': '10', 'suite': 'Hearts', 'value': 10},
    {'name': 'Jack', 'suite': 'Spades', 'value': 11}, {'name': 'Jack', 'suite': 'Clubs', 'value': 11},
    {'name': 'Jack', 'suite': 'Diamonds', 'value': 11}, {'name': 'Jack', 'suite': 'Hearts', 'value': 11},
    {'name': 'Queen', 'suite': 'Spades', 'value': 12}, {'name': 'Queen', 'suite': 'Clubs', 'value': 12},
    {'name': 'Queen', 'suite': 'Diamonds', 'value': 12}, {'name': 'Queen', 'suite': 'Hearts', 'value': 12},
    {'name': 'King', 'suite': 'Spades', 'value': 13}, {'name': 'King', 'suite': 'Clubs', 'value': 13},
    {'name': 'King', 'suite': 'Diamonds', 'value': 13}, {'name': 'King', 'suite': 'Hearts', 'value': 13}]
    """
    card_names = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
    suites = ("Spades", "Clubs", "Diamonds", "Hearts")
    face_values = {"Jack": 11, "Queen": 12, "King": 13}
    deck = []
    for name in card_names:
        for suite in suites:
            card = {"name": name, "suite": suite}
            if name == "Ace":
                card["value"] = 1
            elif name in ("Jack", "Queen", "King"):
                card["value"] = face_values[name]
            else:
                card["value"] = int(name)
            deck.append(card)
    return deck


def main():
    """
    Drive the program.
    """
    print("Welcome to the module")


if __name__ == "__main__":
    main()
