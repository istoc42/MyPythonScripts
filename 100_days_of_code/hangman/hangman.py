#Step 4

import random
from hangman_art import *
from hangman_words import *

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Print the logo
print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

wrong_guesses = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()


    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
          
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f'The letter {guess} is not in the word.')
        print(f'You have {lives} lives remaining...')
        if guess in wrong_guesses:
          print(f'You have already guessed {guess}. Wrong guesses: {wrong_guesses}')
        else:
          wrong_guesses += guess

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if lives <= 0:
        end_of_game = True
        print(f"You lose. The answer was {chosen_word}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(f"You win. The answer was {chosen_word}")

    