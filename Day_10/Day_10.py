from art import logo

continue_calculating = True


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

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

while continue_calculating:
    operation_symbol = input("Pick and operation: ")
    num2 = int(input("What's the next number?: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    num1 = answer

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continue_with_answer = input(f"Type 'y' to continue with {answer}, or type 'n' to exit.: ")
    if continue_with_answer == 'n':
        continue_calculating = False