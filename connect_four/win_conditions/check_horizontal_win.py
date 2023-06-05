def check_horizontal_win(board: dict, chosen_row: int, columns: int) -> bool:
    """
    Check if the player has connected four pieces horizontally.

    :param board: a dictionary representing the game board
    :param chosen_row: an integer representing the desired row on the game board
    :param columns: an integer representing the number of columns on the game board
    :precondition: board must be a dictionary
    :precondition: chosen_row must be an integer
    :precondition: columns must be an integer
    :precondition: columns must be positive
    :precondition: columns must be equal to the number of the rows on the game board
    :postcondition: checks if four adjacent spaces in a column on the game board are all the same and not the default
    :return: True if four adjacent spaces in a row on the game board are all the same and not the default, else false
    :raises TypeError: if board is not a dictionary
    :raises TypeError: if chosen_row is not an integer
    :raises TypeError: if columns is not an integer
    :raises ValueError: if columns is not positive
    >>> test_board_win = {(1, 1): '[ ]', (1, 2): '[O]', (1, 3): '[ ]', (1, 4): '[O]', (2, 1): '[O]',
    ... (2, 2): '[O]', (2, 3): '[O]', (2, 4): '[O]'}
    >>> check_horizontal_win(test_board_win, 2, 4)
    True
    >>> test_board_no_win = {(1, 1): '[ ]', (1, 2): '[ ]', (1, 3): '[ ]', (1, 4): '[O]', (2, 1): '[O]',
    ... (2, 2): '[ ]', (2, 3): '[O]', (2, 4): '[O]'}
    >>> check_horizontal_win(test_board_no_win, 1, 4)
    False
    >>> test_board_not_enough_columns = {(1, 1): '[ ]', (1, 2): '[ ]', (1, 3): '[ ]', (1, 4): '[O]', (2, 1): '[O]',
    ... (2, 2): '[ ]', (2, 3): '[O]', (2, 4): '[O]'}
    >>> check_horizontal_win(test_board_not_enough_columns, 1, 3)
    False
    """
    if type(board) is not dict:
        raise TypeError("The board must be represented with a dictionary.")
    if type(chosen_row) is not int or type(columns) is not int:
        raise TypeError("The chosen column and number of columns must both be integers")
    if columns < 0:
        raise ValueError("The number of columns must be positive")
    current_symbol = "[ ]"
    for column in range(1, columns + 1):
        current_space = board.get((chosen_row, column))
        if current_space != current_symbol:
            current_symbol = current_space
            counter = 1
        elif current_space == current_symbol and current_space is not None and current_space != "[ ]":
            counter += 1
            if counter == 4:
                return True
    return False


def main():
    """
    Drive the program.
    """
    print("Welcome to the module")


if __name__ == "__main__":
    main()
