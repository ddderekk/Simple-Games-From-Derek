from war.create_deck_war import create_deck_war
import random
from blackjack.show_hand import show_hand


def war() -> None:
    """
    Play war in the terminal.
    """
    print("It's the card game War. Brag to your friends if you can win the game within the round limit."
          "If you are unfamiliar with the game, "
          "the rules are here: https://bicyclecards.com/how-to-play/war")
    deck = create_deck_war()
    random.shuffle(deck)
    random.shuffle(deck)
    player_deck = []
    opponent_deck = []
    while len(deck) > 0:
        player_deck.append(deck.pop())
        opponent_deck.append(deck.pop())

    draw_counter = 0
    while len(player_deck) > 0 and len(opponent_deck) > 0 and draw_counter != 120:
        input("Type something to place a card in the middle:")
        player_card = player_deck.pop(0)
        opponent_card = opponent_deck.pop(0)
        print(f"Your card is {show_hand([player_card])}. Value: {player_card.get('value')}")
        print(f"Your opponent's card is {show_hand([opponent_card])}. Value: {opponent_card.get('value')}\n")

        if player_card.get("value") > opponent_card.get("value"):
            print("You win! You get both cards.")
            print(f"You add the {show_hand([player_card])} and "
                  f"{show_hand([opponent_card])} to the bottom of your deck.\n")
            player_deck.append(player_card)
            player_deck.append(opponent_card)

        elif player_card.get("value") < opponent_card.get("value"):
            print("You lose! Your opponent gets both cards.")
            print(f"They add the {show_hand([player_card])} and "
                  f"{show_hand([opponent_card])} to the bottom of their deck.\n")
            opponent_deck.append(opponent_card)
            opponent_deck.append(player_card)

        else:
            print("It's War!")
            continue_war = True
            player_pool = []
            opponent_pool = []
            while continue_war:
                input("Type something to place one card face-up and one face-down in the middle:")
                player_pool.append(player_deck.pop(0))
                player_pool.append(player_deck.pop(0))
                opponent_pool.append(opponent_deck.pop(0))
                opponent_pool.append(opponent_deck.pop(0))
                print(f"Your face-up card is {show_hand([player_pool[-1]])}. Value: {player_pool[-1].get('value')}")
                print(f"Your opponent's face-up card is {show_hand([opponent_pool[-1]])}. "
                      f"Value: {opponent_pool[-1].get('value')}\n")

                if player_pool[-1].get('value') > opponent_pool[-1].get('value'):
                    print(f"You won! You get all {len(player_pool) + len(opponent_pool) + 2} cards!\n")
                    player_deck += player_pool + opponent_pool + [player_card] + [opponent_card]
                    continue_war = False

                elif player_pool[-1].get('value') < opponent_pool[-1].get('value'):
                    print(f"You lose! Your opponent gets all {len(player_pool) + len(opponent_pool) + 2} cards!\n")
                    opponent_deck += player_pool + opponent_pool + [player_card] + [opponent_card]
                    continue_war = False
                else:
                    print("The cards are equally matched! The war continues!.\n")
        draw_counter += 1

    if draw_counter == 120:
        print("This is taking too long! It's a Draw!")
    elif len(player_deck) > 0:
        print("You win! Good job!")
    else:
        print("You lose! Skill issue.")


def main():
    """
    Drive the program.
    """
    war()


if __name__ == "__main__":
    main()
