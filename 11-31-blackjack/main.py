import random
from art import logo

# Blackjack Project

# Our Blackjack House Rules

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []


def show_cards():
    print(f"This is your cards {player_cards} and total score is {calculate_total(player_cards)}")
    print(f"This is one of dealer's card {dealer_cards[0]}, {dealer_cards}")


def calculate_total(cards_to_calculate):
    total_score = 0
    for card_score in cards_to_calculate:
        total_score += card_score
    return total_score


def draw_a_card(deck):
    random_card = random.choice(cards)
    deck.append(random_card)
# start of the game


print(logo)
print("Welcome to blackjack!")
for start_card in range(2):
    draw_a_card(player_cards)
    draw_a_card(dealer_cards)
show_cards()


def player_score():
    return calculate_total(player_cards)


def dealer_score():
    return calculate_total(dealer_cards)


stand_or_hit = input("Would you like to hit another card (y) or stand? (n): ")
if stand_or_hit == "y":
    draw_a_card(player_cards)
    player_score()
    show_cards()
else:
    print(f"Your total score is {player_score()}")
    while dealer_score() < 18:
        print(f"dealer's cards score before one cycle {dealer_score()}")
        draw_a_card(dealer_cards)
        print(f"dealers cards in cycle {dealer_cards}")
        dealer_score()
        print(f"TEST {dealer_cards}")
        if dealer_score() > 21 and 11 in dealer_cards:
            dealer_cards = sorted(dealer_cards)
            dealer_cards[-1] = 1
            print(dealer_cards)
            print(f"dealer's score after the whole cycle {dealer_score()}")

print(f"your total card score is {player_score()}")
print(f"dealer's total card score is {dealer_score()}")
