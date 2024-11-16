# blackjack.py
# v0.3.1

import random, time

def create_deck():
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['♠️', '♣️', '♥️', '♦️', ]
    deck = [(value, suit) for suit in suits for value in values]
    return deck

def hand_value(hand):
    value = 0
    aces = 0
    for rank, _ in hand:
        if rank in ('J', 'Q', 'K'):
            value += 10
        elif rank == 'A':
            value += 11
            aces += 1
        else:
            value += int(rank)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def show_hand(hand, name, show_hole=True):
    hand_string = ', '.join([card[0] + card[1] for card in hand]) if show_hole else f'{hand[0][0]}{hand[0][1]}, ?'
    print(f'{name} hand: {hand_string} (total: {hand_value(hand)})' if show_hole else f'{name} hand: {hand_string}')


def play(deck=create_deck()):
    random.shuffle(deck)
    player_hand, dealer_hand = [deck.pop() for _ in range(2)], [deck.pop() for _ in range(2)]
    player_turn = True
    show_hand(player_hand, 'Your')
    show_hand(dealer_hand, "Dealer's", False)
    print()
    time.sleep(2)

    # Blackjack
    if hand_value(player_hand) == 21:
        print("It's a blackjack!")
        time.sleep(1)
        show_hand(dealer_hand, "Dealer's")
        if hand_value(dealer_hand) == 21:
            print("It's a push.\n")
            return 'push'
        else:
            print('You win!\n')
            return 'blackjack'

    # Player's turn
    while player_turn:
        action = input('Would you like to (h)it or (s)tand?  ').lower()
        if action == 'h':
            new_card = deck.pop()
            player_hand.append(new_card)
            print(f'You drew a {"".join(new_card)}.')
            show_hand(player_hand, 'Your')
            if hand_value(player_hand) > 21:
                print('You bust! Dealer wins.\n')
                return 'loss'
        elif action == 's':
            print(f'You stand with {hand_value(player_hand)}.')
            player_turn = False
        else:
            print('Invalid action.')
        print()
        time.sleep(1)
    
    # Dealer's turn
    print("Dealer's turn.")
    show_hand(dealer_hand, "Dealer's")
    time.sleep(1)
    while hand_value(dealer_hand) < 17:
        new_card = deck.pop()
        dealer_hand.append(new_card)
        print(f'The dealer draws a {"".join(new_card)}.')
        show_hand(dealer_hand, 'Dealer')
        if hand_value(dealer_hand) > 21:
            print('Dealer busts! You win.\n')
            return 'win'
    print(f'Dealer stands with {hand_value(dealer_hand)}.\n')
    time.sleep(1)

    # results
    show_hand(player_hand, 'Your')
    show_hand(dealer_hand, "Dealer's")
    time.sleep(1)
    if hand_value(player_hand) > hand_value(dealer_hand):
        print('You win!\n')
        return 'win'
    elif hand_value(player_hand) < hand_value(dealer_hand):
        print('You lose.\n')
        return 'loss'
    else:
        print("It's a push.\n")
        return 'push'

if __name__ == "__main__":
    print(f'output: {play()}')
