def get_player_choice(valid_inputs: tuple, prompt: str) -> str:
    """
    Take valid user input.

    :param valid_inputs: a tuple that represents the valid choices users can make.
    :param prompt: a string for prompting the user
    :precondition: acceptable_choices must be a tuple
    :precondition: acceptable_choices must only contain strings
    :precondition: prompt must be a string
    :postcondition: takes valid user input
    :return: the valid user input as a string
    :raises TypeError: if valid_inputs is not a tuple
    :raises TypeError: if prompt is not a string
    :raises TypeError: if valid_inputs contains an element that is not a string
    """
    if type(valid_inputs) is not tuple:
        raise TypeError("Valid inputs must be represented as a tuple.")
    for choice in valid_inputs:
        if type(choice) is not str:
            raise TypeError("Valid inputs must be represented as a tuple containing only strings.")
    if type(prompt) is not str:
        raise TypeError("The prompt for the user must be a string.")
    user_input = ""
    while user_input not in valid_inputs:
        user_input = input(f"{prompt}:")
        if user_input not in valid_inputs:
            print("You can't do that.")
    return user_input


def main():
    """
    Drive the program.
    """
    print("Welcome to the module")


if __name__ == "__main__":
    main()
