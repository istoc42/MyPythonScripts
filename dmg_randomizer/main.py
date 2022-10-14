from random import choice
from table_roller import Table_roller
import tables

tb = Table_roller()

# TODO Choose between location based or event based encounters
encounter_type_choice = input(
    "What kind of encounter would you like to generate? \n1. Location based encounter. \n2. Event based encounter.\n(1/2?): ")

if encounter_type_choice == "1":
    print("\nYou have chosen a Location Based Encounter.\n")

    # LOCATION BASED ADVENTURES

    # Identify the party's goals
    # Dungeon goals
    # Wilderness goals
    # Other goals
    party_goals = tb.get_party_goals()

    # Identify important NPCs
    # Adventure villains
    # Adventure allies
    # Adventure patrons
    important_npcs = tb.get_important_npcs()

    # TODO Flesh out location details

    # Find the ideal introduction and consider the ideal climax
    # Adventure intro
    # Adventure climax
    intro_and_climax = tb.get_intro_and_climax()

# TODO Plan encounters
elif encounter_type_choice == "2":
    print("\nYou have chosen an Event Based Encounter.\n")
# EVENT BASED ADVENTURES

# TODO 1. Start with a villain

# TODO 2. Determine the villains actions
# Event based villian actions

# TODO 3. Determine the party's goals
# Event based goals

# TODO 4. Identify important NPCs
# Adventure villains
# Adventure allies
# Adventure patrons

# TODO 5. Anticipate the villain's reactions

# TODO 6. Detail key locations
# Random dungeon?

# TODO 7. Choose and intro and climax
# Adventure intro
# Adventure climax

# TODO 8. Plan encounters
