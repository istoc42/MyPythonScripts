#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for letter in range(1, nr_letters + 1):
    index = random.randint(0, len(letters) - 1)
    password.append(letters[index])

for symbol in range(1, nr_symbols + 1):
    index2 = random.randint(0, len(symbols) - 1)
    password.append(symbols[index2])

for number in range(1, nr_numbers + 1):
    index3 = random.randint(0, len(numbers) - 1)
    password.append(numbers[index3])

password_string = ''.join(password)

print("Characters generated: " + password_string)

random_password = random.sample(password, len(password))

random_password_string = ''.join(random_password)

print(f'Your new password is: {random_password_string}')
