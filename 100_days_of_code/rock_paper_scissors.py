#! python3

# rock_paper_scissors.py - A rock paper scissors game

import random, time

# ASCII art for the choices
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store user input
print("Hello! Let's play Rock-Paper-Scissors!\n")

while True: # Main game loop
    player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    if player_choice == "0":
        player_choice = rock
        print(f'You have chosen Rock. {rock}')
        break
    elif player_choice == "1":
        player_choice = paper
        print(f'You have chosen Paper. {paper}')
        break
    elif player_choice == "2":
        player_choice = scissors
        print(f'You have chosen Scissors. {scissors}')
        break
    else:
        player_choice = print("Invalid choice. Please try again.")


# Generate random choice for CPU
possible_cpu_choices = [rock, paper, scissors]
possible_cpu_choices_string = ["Rock", "Paper", "Scissors"]

index = random.randint(0, 3) - 1

cpu_choice = possible_cpu_choices[index]
cpu_choice_string = possible_cpu_choices_string[index]

# Compare both choices and provide player feedback
print("I'm thinking...")
time.sleep(3)
print("Okay, I'm ready!")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("Shoot!")
time.sleep(1)

print(f"I have chosen {possible_cpu_choices_string[index]}" + cpu_choice)

if player_choice == rock:
    if cpu_choice == rock:
        print("It's a tie! Nobody wins!")
    elif cpu_choice == paper:
        print("Paper beats Rock! You lose!")
    elif cpu_choice == scissors:
        print("Rock beats Scissors! You win!")
elif player_choice == paper:
    if cpu_choice == rock:
        print("Paper beats Rock! You win!")
    elif cpu_choice == paper:
        print("It's a tie! Nobody wins!")
    elif cpu_choice == scissors:
        print("Scissors beats Paper! You lose!")
if player_choice == scissors:
    if cpu_choice == rock:
        print("Rock beats Scissors! You lose!")
    elif cpu_choice == paper:
        print("Sicssors beats Paper! You win!")
    elif cpu_choice == scissors:
        print("It's a tie! Nobody wins!")