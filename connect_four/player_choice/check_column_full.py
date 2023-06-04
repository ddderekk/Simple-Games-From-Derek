def check_column_full(board: dict, chosen_column: int, rows: int) -> bool:
    """
    Check if the column on the game board is full.

    :param board: a dictionary representing the game board
    :param chosen_column: an integer representing the desired column on the game board
    :param rows: an integer representing the number of rows on the game board
    :precondition: board must be a dictionary
    :precondition: chosen_column must be an integer
    :precondition: rows must be an integer
    :precondition: rows must be positive
    :postcondition: checks if the column on the board is full
    :return: True if the column on the board is full, else false
    :raises TypeError: if board is not a dictionary
    :raises TypeError: if chosen_column is not an integer
    :raises TypeError: if rows is not an integer
    :raises ValueError: if rows is not positive
    >>> test_board_empty = {(1, 1): '[ ]', (2, 1): '[ ]', (3, 1): '[ ]'}
    >>> check_column_full(test_board_empty, 1, 3)
    False
    >>> test_board_full = {(1, 1): '[O]', (1, 2): '[O]', (2, 1): '[O]', (2, 2): '[O]'}
    >>> check_column_full(test_board_empty, 2, 2)
    True
    >>> test_board_mix = {(1, 1): '[ ]', (1, 2): '[O]', (1, 3): '[O]', (2, 1): '[O]', (2, 2): '[O]', (2, 3): '[ ]',
    ... (3, 1): '[ ]', (3, 2): '[O]', (3, 3): '[O]'}
    >>> check_column_full(test_board_empty, 2, 3)
    True
    """
    if type(board) is not dict:
        raise TypeError("The board must be represented with a dictionary.")
    if type(chosen_column) is not int or type(rows) is not int:
        raise TypeError("The chosen column and number of rows must both be integers")
    if rows < 0:
        raise ValueError("The number of rows must be positive")
    for row in range(1, rows + 1):
        if board.get((row, chosen_column)) == "[ ]":
            return False
    return True


def main():
    """
    Drive the program.
    """
    print("Welcome to the module")


if __name__ == "__main__":
    main()
