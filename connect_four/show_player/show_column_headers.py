def show_column_headers(columns: int) -> None:
    """
    Print numbered headers for each column.

    :param columns: an integer representing the number of columns
    :precondition: columns must be an integer
    :precondition: columns must be positive
    :postcondition: prints numbered headers for each column
    :raises TypeError: if columns is not an integer
    :raises ValueError: if columns is not positive
    >>> show_column_headers(5) # doctest: +NORMALIZE_WHITESPACE
     1   2   3   4   5
    >>> show_column_headers(0) # doctest: +NORMALIZE_WHITESPACE

    >>> show_column_headers(1) # doctest: +NORMALIZE_WHITESPACE
     1
    """
    if type(columns) is not int:
        raise TypeError("The number of columns must be an integer.")
    if columns < 0:
        raise ValueError("The number of columns must be positive")
    for column in range(1, columns + 1):
        print(f" {str(column)} ", end=' ')


def main():
    """
    Drive the program.
    """
    print("Welcome to the module")


if __name__ == "__main__":
    main()
