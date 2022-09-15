import random
from game_data import *
from art import *

print(logo)

# Randomly select two objects from game_data.py
def select_random_object():
    # Choose a number between 1 - 50
    data_index = random.randrange(1, 50)
    # Assign it to an index variable
    print("Data index is " + str(data_index))
    return data_index

# Function to compare followers of each choice and return the winner
def compare_followers(comparison_a, comparison_b):
    followers_a = comparison_a['follower_count']
    followers_b = comparison_b['follower_count']

    if followers_a > followers_b:
        result = "A"
        return result
    else:
        result = "B"
        return result

points = 0
while True:
    first_id = select_random_object()
    second_id = select_random_object()

    print()

    # Check if both objects are the same, if they are, run function again.
    while True:
        if first_id == second_id:
            second_id = select_random_object()
        else:
            break

    # Assign each selected object to a seperate variable named option_a and option_b
    option_a = data[first_id]
    option_b = data[second_id]

    # Print the information for option_a, followed by the vs art, followed by the info for option_b

    print("Compare A: " + str(option_a['name']) + ", a " + str(option_a['description']) + " from " + str(option_a['country']) + ".")

    print(vs)

    print("Against B: " + str(option_b['name']) + ", a " + str(option_b['description']) + " from " + str(option_b['country']) + ".")



    # print the followers of each option
    # print((str(option_a['name'] + " has " + str(option_a['follower_count']) + " million followers")))
    # print((str(option_b['name'] + " has " + str(option_b['follower_count']) + " million followers")))

    # Assign the winner to a variable
    winner = compare_followers(option_a, option_b)

    # Print message based on the winner
    if winner == "A":
        print(str(option_a['name'] + " has the most followers"))
    else:
        print(str(option_b['name'] + " has the most followers"))

    # TODO Ask player to choose if either A or B has the highest followers 
    while True:
        answer = input("Who has the most followers? (A/B) ").upper()

        if answer == "A" or answer == "B":
            break
        else:
            print("Invalid answer. Please try again.")

    if answer == winner:
        # print((str(option_a['name'] + " has " + str(option_a['follower_count']) + " million followers")))
        # print((str(option_b['name'] + " has " + str(option_b['follower_count']) + " million followers")))
        print("You were correct! Well done!")
        points += 1
        print("You scored 1 point. Total points: " + str(points)) 
    else:
        print("You guessed wrong. Game over.")
        print("You scored " + str(points) + " points.")
        break



# TODO Change the winner to option A and select a new option B 