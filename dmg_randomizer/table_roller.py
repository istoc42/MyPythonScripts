from random import choice
from tables import *


class Table_roller:
    def get_important_npcs(self):
        print("IMPORTANT NPCS: \n")
        new_adventure_villian = choice(adventure_villians)
        new_adventure_ally = choice(adventure_allies)
        new_adventure_patron = choice(adventure_patrons)
        print(f'Adventure villian: {new_adventure_villian}')
        print(f'Adventure ally: {new_adventure_ally}')
        print(f'Adventure patron: {new_adventure_patron} \n')

    def get_party_goals(self):
        print("PARTY GOALS: \n")
        new_dungeon_goal = choice(dungeon_goals)
        new_wilderness_goal = choice(wilderness_goals)
        new_other_goal = choice(other_goals)
        print(f'Dungeon goal: {new_dungeon_goal}')
        print(f'Wilderness goal: {new_wilderness_goal}')
        print(f'Other goal: {new_other_goal} \n')

    def get_intro_and_climax(self):
        print("INTRODUCTION AND CLIMAX: \n")
        new_adventure_intro = choice(adventure_intro)
        new_adventure_climax = choice(adventure_climax)
        print(f'Adventure intro: {new_adventure_intro}')
        print(f'Adventure climax: {new_adventure_climax} \n')
