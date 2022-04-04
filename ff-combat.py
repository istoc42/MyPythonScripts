#! python3

# ff-combat.py - A program to simulate the combat mechanics from the Fighting
#                Fantasy books.

import random, time 

roll_one = random.randint(1, 6)
roll_two = random.randint(2, 12)

# Declare global variables for the players skill, stamina and luck.
initial_player_skill = roll_one + 6
initial_player_stamina = roll_two + 12
initial_player_luck = roll_one + 6

print(f"""
Initial player stats: \n
Skill: {initial_player_skill}
Stamina: {initial_player_stamina}
Luck: {initial_player_luck}
""")

# START OF COMBAT

# Player stats
player_skill = int(initial_player_skill)
player_stamina = int(initial_player_stamina)

# Goblin stats
goblin_skill = int(6)
goblin_stamina = int(6)

print('\nYou are attacked by a goblin!')
print(f'\nGoblin Skill: {goblin_skill} \nGoblin Stamina: {goblin_stamina}')
input('\nPress any key to Attack!\n')

r = 1

while goblin_stamina > 0 and player_stamina > 0:
    print(f'Round {r}:')
    player_attack = random.randint(2, 12) + player_skill
    print(f'Player attack: {player_attack}')
    goblin_attack = random.randint(2, 12) + goblin_skill
    print(f'Goblin attack: {goblin_attack}')

    if player_attack > goblin_attack:
        goblin_stamina = goblin_stamina - 2
        print('You hit the goblin!')
        print(f'Player stamina: {player_stamina}, Goblin stamina: {goblin_stamina}\n')
        
    else:
        player_stamina = player_stamina - 2
        print('The goblin hits you!')
        print(f'Player stamina: {player_stamina}, Goblin stamina: {goblin_stamina}\n')
        
    r = r + 1
    time.sleep(1)

if goblin_stamina == 0:
    print('You killed the goblin!')
else:
    print('You were killed!')

r = 1
