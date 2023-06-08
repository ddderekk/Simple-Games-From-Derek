import random
from blackjack import check_natural, create_deck, place_wager, show_hand, sum_aces, sum_non_aces
from common_features.get_player_choice import get_player_choice


def blackjack() -> None:
    print("Play until you run out of money or get bored."
          " Maybe show your friends how much virtual money you won."
          " The option to double down or split pairs is not available.\n")
    deck = create_deck.create_deck()
    random.shuffle(deck)
    player_money = 500
    while player_money > 0:
        if len(deck) < 12:
            deck = create_deck.create_deck()
            random.shuffle(deck)
        print(f"You have ${player_money}.\n")
        wager = place_wager.place_wager(player_money)
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        insurance = False
        insurance_wager = 0
        if dealer_hand[0]["name"] == "Ace":
            print("The dealer's face-up card is an Ace.")
            insurance_choice = get_player_choice(("Y", "y", "N", "n"), "Do you want to take Insurance?(Y/N)")
            if insurance_choice == "Y" or insurance_choice == "y":
                insurance = True
                print("You can wager up to half of your original wager.")
                insurance_wager = place_wager.place_wager(int(wager/2))
        if check_natural.check_natural(player_hand) and not check_natural.check_natural(dealer_hand):
            print(f"\nYou got a Blackjack! \nYour hand was {show_hand.show_hand(player_hand)}. \n"
                  f"You get ${int(1.5 * wager)}.\n")
            player_money += int(1.5 * wager)
        elif not check_natural.check_natural(player_hand) and check_natural.check_natural(dealer_hand):
            print(f"\nThe dealer got a Blackjack! The dealer's hand was {show_hand.show_hand(dealer_hand)}."
                  f" \nYour hand was {show_hand.show_hand(player_hand)}.")
            player_money -= wager
            if insurance:
                player_money += 2 * insurance_wager
                print(f"You get ${int(2 * insurance_wager)} from your insurance.\n")
        elif check_natural.check_natural(player_hand) and check_natural.check_natural(dealer_hand):
            print(f"\nBoth you and the dealer got Blackjacks! Here's your money back. \n"
                  f"The dealer's hand was {show_hand.show_hand(dealer_hand)}. \n"
                  f"Your hand was {show_hand.show_hand(player_hand)}.\n")
            if insurance:
                player_money += 2 * insurance_wager
                print(f"You get ${int(2 * insurance_wager)} from your insurance.\n")

        else:
            print(f"The dealer's face-up card is {show_hand.show_hand([dealer_hand[0]])}.")
            if insurance:
                player_money -= insurance_wager
                print(f"The dealer didn't have a Blackjack. You lose ${insurance_wager}.")

            continue_drawing = True
            while continue_drawing:
                print(f"\nYour hand is {show_hand.show_hand(player_hand)}."
                      f"\n Total: {sum_non_aces.sum_non_aces(player_hand) + sum_aces.sum_aces(player_hand)}")
                hit_or_stand = get_player_choice(("Hit", "Stand", "hit", "stand"), "Will you Hit or Stand?")
                if hit_or_stand == "Hit" or hit_or_stand == "hit":
                    player_hand.append(deck.pop())
                else:
                    continue_drawing = False
                if sum_non_aces.sum_non_aces(player_hand) + sum_aces.sum_aces(player_hand) == 21:
                    continue_drawing = False
                    print(f"\nYour hand is {show_hand.show_hand(player_hand)}."
                          f"\n Total: {sum_non_aces.sum_non_aces(player_hand) + sum_aces.sum_aces(player_hand)}")
                elif sum_non_aces.sum_non_aces(player_hand) + sum_aces.sum_aces(player_hand) > 21:
                    continue_drawing = False
                    player_money -= wager

            if sum_non_aces.sum_non_aces(player_hand) + sum_aces.sum_aces(player_hand) <= 21:
                while sum_non_aces.sum_non_aces(dealer_hand) + sum_aces.sum_aces(dealer_hand) < 17:
                    print(f"\nThe dealer's hand is {show_hand.show_hand(dealer_hand)}."
                          f"\n Total: {sum_non_aces.sum_non_aces(dealer_hand) + sum_aces.sum_aces(dealer_hand)}")
                    dealer_hand.append(deck.pop())
                    print(f"The dealer must hit.")

                print(f"\nThe dealer's hand is {show_hand.show_hand(dealer_hand)}."
                      f"\n Total: {sum_non_aces.sum_non_aces(dealer_hand) + sum_aces.sum_aces(dealer_hand)}")

                player_hand_total = sum_non_aces.sum_non_aces(player_hand) + sum_aces.sum_aces(player_hand)
                dealer_hand_total = sum_non_aces.sum_non_aces(dealer_hand) + sum_aces.sum_aces(dealer_hand)
                if player_hand_total > dealer_hand_total or dealer_hand_total > 21:
                    print(f"\nYou won! Your hand was {show_hand.show_hand(player_hand)}. Total:{player_hand_total}\n"
                          f"The dealer's hand was {show_hand.show_hand(dealer_hand)}. Total:{dealer_hand_total}\n"
                          f"You won ${wager}.\n")
                    player_money += wager
                elif player_hand_total < dealer_hand_total:
                    print(f"\nYou lost! Your hand was {show_hand.show_hand(player_hand)}. Total:{player_hand_total}\n"
                          f"The dealer's hand was {show_hand.show_hand(dealer_hand)}. Total:{dealer_hand_total}\n"
                          f"You lose ${wager}.\n")
                    player_money -= wager
                else:
                    print(f"\nA Standoff! Your hand was {show_hand.show_hand(player_hand)}. Total:{player_hand_total}\n"
                          f"The dealer's hand was {show_hand.show_hand(dealer_hand)}. Total:{dealer_hand_total}\n"
                          f"Here's your money back.")
            else:
                print(f"Your hand is {show_hand.show_hand(player_hand)}."
                      f"\n Total: {sum_non_aces.sum_non_aces(player_hand) + sum_aces.sum_aces(player_hand)}\n"
                      f"Your hand is a bust. You lose ${wager}.\n")
    print("You're out of money!")


def main():
    """
    Drive the program.
    """
    blackjack()


if __name__ == "__main__":
    main()
