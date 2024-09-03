# complex mapping of functions
# functions aaa
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

for symbol in operations:  # loops through the operations dictionary
    print(symbol)

operation_symbol = input("Pick a operation from above: ")

# above "function aaa" get called according to the choosen symbols
calculation_function = operations[operation_symbol]

first_answer = calculation_function(n1, n2)  # valued get passed to function

print(first_answer)

# "return" is used to pass result as input to another function

n3 = int(input("Enter third number: "))

operation_symbol = input("Pick another operation from above: ")
# above "function aaa" get called according to the choosen symbols
calculation_function = operations[operation_symbol]

# valued get passed to function
second_answer = calculation_function(first_answer, n3)
# or
second_answer = calculation_function(calculation_function(
    n1, n2), n3)  # valued get passed to function

print(second_answer)