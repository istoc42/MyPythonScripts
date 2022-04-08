from art import *

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(text, shift):
    while run_program:
        if direction == 'encode':
            encrypted_message = ""
            for letter in text:
                if letter in alphabet:
                    new_index = alphabet.index(letter) + shift
                    if new_index >= 26:
                        new_index -= 26
                    encrypted_message += alphabet[new_index]
                else:
                    encrypted_message += letter

            print(encrypted_message)

        elif direction == 'decode':
            decrypted_message = ""
            for letter in text:
                if letter in alphabet:
                    new_index = alphabet.index(letter) - shift
                    if new_index < 0:
                        new_index += 26
                    decrypted_message += alphabet[new_index]
                else:
                    decrypted_message += letter
            print(decrypted_message)

        retry = input("Would you like to restart the program? Y/N\n").lower()

        if retry == "y":
            continue
        else: 
            print("Closing program...")
            run_program = False

caeser(text, shift)

