from itertools import cycle
from common_features import check_board_full, get_player_choice, make_board, show_board, show_column_headers
from connect_four.player_choice import check_column_full, find_open_space
from connect_four.win_conditions import check_vertical_win, check_horizontal_win, check_diagonal_win


def connect_four():
    """
    Play connect four in terminal.
    """
    player_one = {"name": "\033[31mPlayer 1\033[0;0m", "symbol": "[\033[31mo\033[0;0m]"}
    player_two = {"name": "\033[93mPlayer 2\033[0;0m", "symbol": "[\033[93mo\033[0;0m]"}
    player_loop = cycle((player_one, player_two))
    valid_choices = ("1", "2", "3", "4", "5", "6", "7")
    board = make_board.make_board_numbered(7, 7)
    show_column_headers.show_column_headers(7)
    show_board.show_board(board, 7, 7)
    game_finished = False
    while not game_finished:
        current_player = next(player_loop)
        print(f"\n{current_player['name']}, it's your turn!")
        chosen_column = int(get_player_choice.get_player_choice
                            (valid_choices, "What column do you want to drop your token?"))
        if not check_column_full.check_column_full(board, chosen_column, 7):
            chosen_row = find_open_space.find_open_space(board, chosen_column, 7)[0]
            board[(chosen_row, chosen_column)] = current_player["symbol"]
            show_column_headers.show_column_headers(7)
            show_board.show_board(board, 7, 7)

            game_finished = check_board_full.check_board_full(board, "[ ]") or \
                check_vertical_win.check_vertical_win(board, chosen_column, 7) or \
                check_horizontal_win.check_horizontal_win(board, chosen_row, 7) or \
                check_diagonal_win.check_diagonal_win_up(board, chosen_row, chosen_column) or \
                check_diagonal_win.check_diagonal_win_down(board, chosen_row, chosen_column)
        else:
            print("That column is full!")
            show_column_headers.show_column_headers(7)
            show_board.show_board(board, 7, 7)
            next(player_loop)
    if check_board_full.check_board_full(board, "[ ]"):
        print("\nIt's a draw!")
    else:
        next(player_loop)
        print(f"\n{next(player_loop)['name']} wins!")


def main():
    """
    Drive the program.
    """
    connect_four()


if __name__ == "__main__":
    main()
