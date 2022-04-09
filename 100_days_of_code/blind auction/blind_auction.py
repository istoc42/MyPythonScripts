from art import *
import os

print(logo)

auction = {}

while True:
    #Ask for name input
    bidder_name = input("Please enter the name of the bidder: \n")

    #Ask for bid price
    bid_price = input("Please enter the bid price: \n£")

    #Add name and bid into a dicitonary as a key and value pair
    auction[bidder_name] = bid_price

    #Ask if there are other users who want to bid
    new_bid = input("Are there any other bidders? (Y/N)\n").lower()
    if new_bid == "y":
        #If yes, Clear the screen and loop back to name input
        os.system('cls')
        continue
    else:
        break

#If no, Find the highest bidder and declare them the winner
highest_bidder = max(auction, key=auction.get)
highest_bid = auction[highest_bidder]

print(f"The highest bidder was {highest_bidder}, with a bid of £{highest_bid}. Congratulations!")