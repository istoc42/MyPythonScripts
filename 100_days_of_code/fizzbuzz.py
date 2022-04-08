# Loop through every number from 1 to 100
for number in range(1, 101):
    # TODO: Check is the number is divisible by 3
    if number % 3 == 0 and number % 5 ==0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    # TODO: Check if number is divisible by 5
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
