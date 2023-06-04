def check_board_full(board: dict, blank_space: str) -> bool:
    """
    Check if the game board is full.

    :param board: a dictionary representing the game board
    :param blank_space: a string representing the default value of a space on the board
    :precondition: board must be a dictionary
    :precondition: blank_space must be a string
    :postcondition: checks if all values in the board are their default values
    :return: True if no values in board are their default values, else False
    :raises TypeError: if board is not a dictionary
    :raises TypeError: if blank_space is not a string
    >>> check_board_full({1: "[ ]", 2: "[O]", 3: "[O]"}, "[ ]")
    False
    >>> check_board_full({1: "[O]", 2: "[O]", 3: "[O]"}, "[ ]")
    True
    >>> check_board_full({1: "[ ]", 2: "[ ]", 3: "[ ]"}, "[ ]")
    False
    """
    if type(board) is not dict:
        raise TypeError("The board must be represented by a dictionary")
    if type(blank_space) is not str:
        raise TypeError("Blank spaces on the board must be strings")
    for space in board.values():
        if space == blank_space:
            return False
    return True


def main():
    """
    Drive the program.
    """
    print("Welcome to the module")


if __name__ == "__main__":
    main()
