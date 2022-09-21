from concurrent.futures import process


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}

# Function to print out remaining resources
def resource_report():
    print("Resources remaining: ")
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "ml")
    print(f'Money: £{resources["money"]:.2f}')

# Function that checks the required resources against the remaining resources
def check_resources(drink_choice):
    coffee = str(drink_choice)
    # Check if each resource is greater than or equal to the required amount
    if resources["water"] >= MENU[coffee]["ingredients"]['water']:
        if resources["milk"] >= MENU[coffee]["ingredients"]['milk']:
            if resources["coffee"] >= MENU[coffee]["ingredients"]['coffee']:
                resources_result = True
                return resources_result
            else:
                print("Sorry. There is not enough coffee.")
        else:
            print("Sorry. There is not enough milk.")
    else:
        print("Sorry. There is not enough water.")

# 5. Function to process coins
def process_coins(coffee):
    #  5a. Check that resources are sufficient then prompt user to insert coins.
    coffee_price = MENU[coffee]["cost"]
    print(f"Price: £{coffee_price:.2f}. Please insert coins.")
    
    tens = input("How many 10p's: ")
    twenties = input("How many 20p's: ")
    fifties = input("How many 50p's: ")
    pounds = input("How many £1's: ")

    #  5c. Calculate the monetary value of coins.
    tens = 0.10 * float(tens)
    twenties = 0.20 * float(twenties)
    fifties = 0.5 * float(fifties)
    pounds = 1 * float(pounds)

    amount_inserted = tens + twenties + fifties + pounds

    print(f'Coins inserted: £{amount_inserted:.2f}.')

    # 6a. Check that the user has inserted enough money.
    
    if amount_inserted > coffee_price:
        # 6c. Give user change if too much money used. Rounded to 2 decimal places.
        change = amount_inserted - coffee_price
        resources["money"] += amount_inserted
        resources["money"] -= change
        print(f'Thank you. Money added to resources. Here is your change: £{change:.2f}.')
        return True
    elif amount_inserted == coffee_price:
        # 6b. Add money to resources.
        resources["money"] += amount_inserted
        print(f'Thank you. Money added to resources. Total money in machine: £{resources["money"]:.2f}.')
        return True
    else:
        print("Not enough money.")
        return False
       

def make_coffee(coffee, check_coins):
    #  7a. If all previous stages successful, deduct resources to make the drink
    if check_coins:
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
        # 7b. "Print" the drink.
        print(f"Enjoy your {coffee}!")
    else:
        return False


# 1b: The prompt should show every time after completing an action
while True:
    # 1: Prompt user to make decision (espresso/latte/cappuccino?)
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # 1a: Check input and decide what to do next
    if user_choice == "report":
        # 3a: Print a report that shows the current resource values.
        resource_report()
    elif user_choice == "espresso":
        coffee = "espresso"
        if check_resources(coffee):
            check_coins = process_coins(coffee)
        else:
            continue
        make_coffee(coffee, check_coins)
    elif user_choice == "latte":
        coffee = "latte"
        if check_resources(coffee):
            check_coins = process_coins(coffee)
        else:
            continue
        make_coffee(coffee, check_coins)
    elif user_choice == "cappuccino":
        coffee = "cappuccino"
        if check_resources(coffee):
            check_coins = process_coins(coffee)
        else:
            continue
        make_coffee(coffee, check_coins)
    elif user_choice == "off":
        # 2. Command to turn machine off and exit the script.
        print("Shutting down...")
        exit()
    else:
        print("Invalid choice. Please try again.")