#! python3

# clickbait.py

import random

OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania', 'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent', 'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado', 'Plastic Straw','Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement', 'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']

def main():
    print('Clickbait Headline Generator')

    print('Our website needs to trick people into looking at ads!')

    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            numberOfHeadlines = int(response)
            break

    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1, 8)

        

