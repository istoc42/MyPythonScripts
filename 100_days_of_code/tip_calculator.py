#! python3

# tip_calculator.py - A calculator to work how how much to tip.

# If the bill was £150.00, split between 5 people, with 12% tip
# Each person should play (150.00 / 5) * 1.12

print("Welcome to the Tip Calculator.")

# Get values
bill = float(input("What was the total of your bill?\n£"))

people = int(input("How many ways are you splitting the bill?\n"))

percentage = (int(input("What percentage are you leaving as a tip? 10, 12 or 15?\n")) / 100) + 1

math = ((bill / people) * percentage)
result = round(math, 2)
final_amount = "{:.2f}".format(math)

print(f'Each person should pay £{final_amount}')