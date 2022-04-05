#! python3

# bmi_calculator.py - A simple calculator to figure out how fat society
#                     thinks you are.

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

heightfloat = float(height)
weightfloat = float(weight)

bmi = (weightfloat / (heightfloat ** 2))

print("Your BMI is: " + str(bmi))

if bmi < 18.5:
  print("You are underweight. Eat a sandwich.")
elif bmi >= 18.5 and bmi <= 24.9:
  print("You are normal. How boring.")
elif bmi >= 25 and bmi <= 29.9:
  print("You are overweight. Put the cookie down.")
elif bmi >= 30 and bmi <= 34.9:
  print("You are obese. More cushion for the pushin'.")
elif bmi > 35:
  print("You are extremely obese. Get on the treadmill, fatty.")
