from deck import Deck
from hand import Hand

def show_hands(player_hand, dealer_hand, reveal_dealer=False):
    print("\nYour hand:", player_hand, "Value:", player_hand.get_value())
    if reveal_dealer:
        print("Dealer's hand:", dealer_hand, "Value:", dealer_hand.get_value())
    else:
        print("Dealer's hand: [", dealer_hand.cards[0], ", *hidden* ]")

def player_turn(deck, player_hand, dealer_hand):
    while True:
        action = input("Do you want to (H)it or (S)tand? ").upper()
        if action == "H":
            player_hand.add_card(deck.deal())
            print("You drew:", player_hand.cards[-1])
            if player_hand.get_value() > 21:
                print("Bust! You've exceeded 21.")
                return False
        elif action == "S":
            print("You stand with a total of", player_hand.get_value())
            return True
        else:
            print("Please enter 'H' to hit or 'S' to stand")
            continue
        show_hands(player_hand, dealer_hand)

def dealer_turn(deck, dealer_hand):
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal())
        print("Dealer draws:", dealer_hand.cards[-1])
    if dealer_hand.get_value() > 21:
        print("Dealer busts! Dealer's total exceeded 21.")
        return False
    return True

def play_blackjack():
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    # Initial deal
    for _ in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

    show_hands(player_hand, dealer_hand)

    # Player turn
    if not player_turn(deck, player_hand, dealer_hand):  # Corrected to include dealer_hand
        print("Dealer wins!")
        return

    # Dealer's turn
    if not dealer_turn(deck, dealer_hand):
        print("You win!")
        return

    # Compare hands
    if player_hand.get_value() > dealer_hand.get_value():
        print("You win!")
    elif player_hand.get_value() < dealer_hand.get_value():
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    while True:
        play_blackjack()
        if input("\nPlay again? (Y/N): ").upper() != "Y":
            break
