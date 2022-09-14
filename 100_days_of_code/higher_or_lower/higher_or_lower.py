import random
from game_data import *
from art import *

print(logo)

# Randomly select two objects from game_data.py
def select_random_object():
    # Choose a number between 1 - 50
    data_index = random.randrange(1, 51)
    # Assign it to an index variable
    print("Data index is " + str(data_index))
    return data_index

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

# TODO Ask player to choose if either A or B has the highest followers 

# TODO Function to compare followers of each choice and return the winner

# TODO Change the winner to option A and select a new option B 