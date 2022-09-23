from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Welcome to the OOP Coffee Machine!")

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    menu_items = menu.get_items()
    user_input = input(f"Please choose a drink: ({menu_items}) ").lower()

    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        is_on = False
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            
