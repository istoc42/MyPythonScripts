#Calculator

from art import logo

#Define operators
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Store operator functions in a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    #User picks first number
    num1 = float(input("What's the first number?: "))

    #Print all operators and user picks one
    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operator from the line above: ")

    for symbol in operations:
        if symbol == operation_symbol:
            func_name = operations[symbol]

    #User picks second number
    num2 = float(input("What's the second number?: "))


    #Calculation
    answer = func_name(num1, num2)

    #Print answer
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    while True:
        continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if continue_calculating == "y":
            num3 = answer
            new_operator = input("Pick an operation: ")
            for symbol in operations:
                if symbol == new_operator:
                    func_name = operations[symbol]
            num4 = float(input("What's the next number?: "))
            answer = func_name(num3, num4)
            print(f"{num3} {new_operator} {num4} = {answer}")
        else:
            calculator()

print(logo)
calculator()