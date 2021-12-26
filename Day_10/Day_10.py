from art import logo

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    continue_calculating = True
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    while continue_calculating:
        operation_symbol = input("Pick an operation.: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_with_answer = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation.: ")
        if continue_with_answer == 'y':
            num1 = answer
        else:
            continue_calculating = False
            calculator()

calculator()