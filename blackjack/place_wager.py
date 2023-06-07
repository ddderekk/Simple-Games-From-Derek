def place_wager(limit: int) -> int:
    """
    Take user wager.

    :param limit: an integer representing the maximum amount
    :precondition: limit must be an integer
    :precondition: limit must be greater than 1
    :postcondition: takes user wager as input and converts it to an integer
    :return: the money the user is willing to wager as an integer
    :raises TypeError: if limit is not an integer
    :raises ValueError: if limit is not greater than 1
    """
    if type(limit) is not int:
        raise TypeError("The limit must be an integer")
    if limit < 1:
        raise ValueError("The limit must be at least 1.")
    wager = "-1"
    is_number = False
    within_limit = False
    while not is_number or not within_limit:
        wager = input("How much do you want to wager?:")
        if not wager.isnumeric() or int(wager) < 1 or int(wager) > limit:
            print("You can't do that.")
        else:
            is_number = True
            within_limit = True
    return int(wager)


def main():
    """
    Drive the program.
    """
    print("Welcome to the module")


if __name__ == "__main__":
    main()
