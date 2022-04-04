import random, sys

print('Dice Roller for D&D')

while True: # Main program loop
    try:
        print('Enter your roll: ')
        diceStr = input('> ') # Prompt to enter the dice roll string
        if diceStr.upper() == 'QUIT':
            print('Thanks for rolling!')
            sys.exit()

        # Clean up the string
        diceStr = diceStr.lower().replace(' ', '')    

        # Find the 'd' in the input string
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the "d" character.')

        # Get the number of dice rolled
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            numberOfDice = 1
        numberOfDice = int(numberOfDice)

        # Check for modifiers
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')

        # Find the number of sides
        if modIndex == -1:
            numberOfSides = diceStr[dIndex + 1 :]
        else: 
            numberOfSides = diceStr[dIndex + 1 : modIndex]
        if not numberOfSides.isdecimal():
            raise Exception('Missing the number of sides.')
        numberOfSides = int(numberOfSides)


        # Find the modifier amount
        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = int(diceStr[modIndex + 1 :])
            if diceStr[modIndex] == '-':
                modAmount = -modAmount

        # Simulate dice rolls
        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfSides)
            rolls.append(rollResult)

        # Display the total
        print('Total:', sum(rolls) + modAmount, '(Each die: ', end='')

        # Display the individual rolls
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        # Display the modifier amount
        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(f', {modSign}{abs(modAmount)}', end='')
        print(')')

    except Exception as exc:
        print('Invalid input. Try again.')
        print('Exception: ' + str(exc))
        continue
