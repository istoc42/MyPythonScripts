#! python3

# email-slicer.py - A program that takes an email address as an
#                   input and return the username and domain.

email = input("Enter your email address: ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"Your username is {username} & your domain is {domain}")

