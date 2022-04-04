#! python3

# talisman-of-death.py - A text adventure game written by Jamie Thompson and Mark Smith

import random, time

# Initialise the Inventory object
# Might need to change to a dictionary later to track number of provisions
inventory = ['Sword', 'Backpack', 'Provisions', 'Fire flares']

# Title
print('TALISMAN OF DEATH\n')
print('Written by Jamie Thompson and Mark Smith')
print('Coded in Python 3.9.1 by Shaun Hudson\n')
input('Press any key to continue!\n')

# Intro

# Roll for stats

roll_one = random.randint(1,6)
roll_two = random.randint(2, 12)

# Roll for SKILL
input('Press any key to roll for your SKILL')
initial_skill_roll = roll_one
initial_skill = initial_skill_roll + 6
print(f'You rolled a {initial_skill_roll}! Your SKILL is {initial_skill}\n')

# Roll for STAMINA
input('Press any key to roll for your STAMINA')
initial_stamina_roll = roll_two
initial_stamina = initial_stamina_roll + 12
print(f'You rolled a {initial_stamina_roll}! Your STAMINA is {initial_stamina}\n')

# Roll for LUCK
input('Press any key to roll for your SKILL')
initial_skill_roll = roll_one
initial_skill = initial_skill_roll + 6
print(f'You rolled a {initial_skill_roll}! Your SKILL is {initial_skill}\n')
