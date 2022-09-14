import random

# Welcome message
print('Welcome to my Number Guessing Game.')
while True:
    # Ask player to select a difficulty. 'Easy' has 10 guesses, 'Hard' has 5 guesses. Assign choice to a variable.
    while True:
        difficulty_choice = input("Please choose a difficulty. (Easy/Hard) ").lower()

        if difficulty_choice == "easy":
            guesses = 10
            print("Easy mode selected. 10 guesses.")
            break
        elif difficulty_choice == "hard":
            guesses = 5
            print("Hard mode selected. 5 guesses.")
            break
        else:
            print("Invalid choice, please choose 'Easy' or 'Hard'.")

    # Determine a random number between 1 and 100
    number_to_guess = random.randrange(1, 101)

    # Uncomment the line below to reveal the number when it's guessed:
    # print("*DEBUG MODE* The number is : " + str(number_to_guess))

    print("I am thinking of a number between 1 and 100...")

    # TODO Create a loop, using the easy or hard variable as the number of iterations. Loop breaks when the iterations runs out or the number is guessed.
    while guesses > 0:
        # Ask for a number
        guessed_number = int(input("What is your guess? "))

        # Check if the guess is correct
        if guessed_number == number_to_guess:
            print("Correct! The number I was thinking of was " + str(number_to_guess) + "!")
            print("You win!")
            break
        else:
            if guessed_number > number_to_guess:
                print("Too high!")
                guesses -= 1
                print("You have " + str(guesses) + " guesses remaining.")
            elif guessed_number < number_to_guess:
                print("Too low!")
                guesses -= 1
                print("You have " + str(guesses) + " guesses remaining.")

    play_again = input("Would you like to play again? (Y/N) ").lower()

    while True:
        if play_again == "y":
            break
        else:
            print("Thank you for playing!")
            break

    if play_again != "y":
        break
    