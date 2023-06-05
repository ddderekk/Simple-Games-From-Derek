def show_board(board: dict, rows: int, columns: int) -> None:
    """
    Print the current game board.

    :param board: a dictionary representing the game board
    :param rows: an integer representing the number of rows on the board
    :param columns: an integer representing the number of rows on the board
    :precondition: board must be a dictionary
    :precondition: rows must be an integer
    :precondition: rows must be positive
    :precondition: columns must be an integer
    :precondition: columns must be positive
    :postcondition: prints current state of game boar
    :raises TypeError: if board is not a dictionary
    :raises TypeError: if rows is not an integer
    :raises TypeError: if columns is not an integer
    :raises ValueError: if rows is not positive
    :raises ValueError: if columns is not positive
    >>> test_board_square = {(1, 1): "[ ]", (1, 2): "[ ]", (2, 1): "[ ]", (2, 2): "[ ]"}
    >>> show_board(test_board_square, 2, 2) # doctest: +NORMALIZE_WHITESPACE
    [ ] [ ]
    [ ] [ ]
    >>> test_board_wide_rectangle = {(1, 1): "[O]", (1, 2): "[ ]", (1, 3): "[O]", (1, 4): "[ ]",
    ... (2, 1): "[O]", (2, 2): "[ ]", (2, 3): "[O]", (2, 4): "[ ]",}
    >>> show_board(test_board_wide_rectangle, 2, 4) # doctest: +NORMALIZE_WHITESPACE
    [O] [ ] [O] [ ]
    [O] [ ] [O] [ ]
    >>> test_board_long_rectangle = {(1, 1): "[O]", (1, 2): "[ ]", (2, 1): "[O]", (2, 2): "[ ]",
    ... (3, 1): "[O]", (3, 2): "[ ]", (4, 1): "[O]", (4, 2): "[ ]"}
    >>> show_board(test_board_long_rectangle, 4, 2) # doctest: +NORMALIZE_WHITESPACE
    [O] [ ]
    [O] [ ]
    [O] [ ]
    [O] [ ]

    """
    if type(board) is not dict:
        raise TypeError("The board must be a dictionary")
    if type(rows) is not int or type(columns) is not int:
        raise TypeError("The rows and columns must both be integers.")
    if rows < 0 or columns < 0:
        raise ValueError("Both rows and columns must be positive integers.")
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            print(board.get((row, column)), end=' ')
        print()


def main():
    """
    Drive the program.
    """
    print("Welcome to the module")


if __name__ == "__main__":
    main()
