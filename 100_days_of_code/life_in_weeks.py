#! python3

# life_in_weeks.py - A calculator that tells you how many days weeks and months you have left.

age = input("What is your current age?\n")
limit = input("How many years do you plan to live?\n")

# 1 year is equivalent to:
# 365 days
# 52 weeks
# 12 months

# For the sake of this program, assume the user will live to 90.

# MATH
days_total = int(limit) * 365
days = int(age) / 365
days_left = round(days_total - days)

weeks_total = int(limit) * 52
weeks = int(age) / 52
weeks_left = round(weeks_total - weeks)

months_total = int(limit) * 12
months = int(age) / 12
months_left = round(months_total - months)

# Print results
print(f'You have {days_left} days left.')
print(f'You have {weeks_left} weeks left.')
print(f'You have {months_left} months left.')