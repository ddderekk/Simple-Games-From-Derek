def make_board_numbered(rows: int, columns: int) -> dict:
    """
    Make a game board labelled with only numbers.

    :param rows: an integer representing the number of rows on the board
    :param columns: an integer representing the number of columns on the board
    :precondition: rows must be an integer
    :precondition: rows must be positive
    :precondition: columns must be an integer
    :precondition: columns must be positive
    :postcondition: creates a dictionary with coordinates as the keys and empty brackets as the values
    :return: a dictionary with coordinates as the keys and empty brackets as the values
    :raises TypeError: if rows is not an integer
    :raises TypeError: if columns is not an integer
    :raises ValueError: if rows is not positive
    :raises ValueError: if columns is not positive
    >>> make_board_numbered(rows=2, columns=2)
    {(1, 1): '[ ]', (1, 2): '[ ]', (2, 1): '[ ]', (2, 2): '[ ]'}
    >>> make_board_numbered(rows=1, columns=3)
    {(1, 1): '[ ]', (1, 2): '[ ]', (1, 3): '[ ]'}
    >>> make_board_numbered(rows=3, columns=2)
    {(1, 1): '[ ]', (1, 2): '[ ]', (2, 1): '[ ]', (2, 2): '[ ]', (3, 1): '[ ]', (3, 2): '[ ]'}
    """
    if type(rows) is not int or type(columns) is not int:
        raise TypeError("Both rows and columns need to be integers")
    if rows < 0 or columns < 0:
        raise ValueError("Both rows and columns must be positive integers")
    return {(row, column): "[ ]" for row in range(1, rows + 1) for column in range(1, columns + 1)}


def main():
    """
    Drive the program.
    """
    print("Welcome to the module")


if __name__ == "__main__":
    main()
