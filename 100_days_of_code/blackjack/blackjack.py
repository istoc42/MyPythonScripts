import random
from art import *

print(logo)

# Deck of cards. 11 = ace
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# input("Press Enter to deal.")

# Player hand lists
user_hand = []
cpu_hand = []

# Deals cards to hands
def deal_card(hand, cards_to_deal):
    for i in range(cards_to_deal):
        card = random.choice(cards)
        hand.append(card)

# Work out the total score of the hand. 21 is represented as "0"
def calculate_score(hand):
    score = sum(hand)

    # Check for a blackjack on the first turn, return a "0"
    if hand[0] + hand[1] == 21:
        result = 0
        return result
    else:  
        if score >= 22 and 11 in user_hand:
            hand.remove(11)
            hand.append(1)
            result = sum(hand)
            return result
        else:
            result = score
            return result

def compare(player_total, cpu_total):
    if player_total == cpu_total:
        result = "Draw!"
        return result
    elif cpu_total == 0:
        result = "Dealer has Blackjack. You lose..."
        return result
    elif player_total == 0:
        result = "Player has blackjack! You win!"
        return result
    elif player_total >= 22:
        result = "You lose..."
        return result
    elif player_total > cpu_total:
        result = "Your total is greater! You win!"
        return result
    elif cpu_total > cpu_total and cpu_total <= 22:
        result = "You lose..."
        return result

while True:
    # Deal opening hands to both players
    deal_card(user_hand, 2)
    deal_card(cpu_hand, 2)

    # Work out player's hand and print it
    user_score = calculate_score(user_hand)
    cpu_score = calculate_score(cpu_hand)
    
    # Print both players hands. Obscures the dealer's second card.
    print("Your hand: " + str(user_hand[0]) + ", " + str(user_hand[1]))
    print("Dealer's hand: " + "?, " + str(cpu_hand[1]))

    if user_score == 21:
        print("Your score is 21!")
        break
    else:
        print("Your score is " + str(user_score))

    # Check if dealer has blackjack when player has blackjack
    if user_score == 0:
        print("Player has Blackjack!")        

    # Player drawing loop
    while True:
        # Ask player to hit or stand
        answer = input("Would you like another card? (Y/N)").lower()

        if answer == "y":
            deal_card(user_hand, 1)
            user_score = calculate_score(user_hand)
            if user_score >= 22:
                print("Your hand: " + str(user_hand))
                print("Your score is " + str(user_score))
                print("You are bust.")
                break
            print("Your hand: " + str(user_hand))
            print("Your score is " + str(user_score))
        else:
            print("You have chosen to stand.")
            # user_score = calculate_score(user_hand)
            # print("Your hand: " + str(user_hand))
            # print("Your score is " + str(user_score))
            break

    print("Dealer's hand: "+ str(cpu_hand))
    print("Dealer's score is " + str(cpu_score))
    


    # Computer drawing loop
    while True:
        if cpu_score == 0:
            print("Dealer has Blackjack")
            break
        elif user_score >= 22:
            print("Dealer stands.")
            break
        elif cpu_score <= 16:
            print("Dealer draws a card...")
            deal_card(cpu_hand, 1)
            cpu_score = calculate_score(cpu_hand)
            if cpu_score >= 22:
                print("Dealer's hand: " + str(cpu_hand))
                print("Dealer's score is " + str(cpu_score))
                print("Dealer is bust.")
                break
            print("Dealer's hand: "+ str(cpu_hand))
            print("Dealer's score is " + str(cpu_score))
        else:
            print("Dealer stands")
            break

    winner = compare(user_score, cpu_score)
    print(winner)

    play_again = input("Would you like to play again? (Y/N)").lower()

    if play_again == "y":
        user_hand.clear()
        cpu_hand.clear()
        continue
    else:
        break
