# we used while loop to proceed  calculation again and again until we do not want
# we used flag too
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

for symbol in operations:  # loops through the operations dictionary
    print(symbol)

should_continue = True  # "should_continue" flag

while should_continue: #while flag is true ; here not specified means true

    operation_symbol = input("Pick a operation: ")

    n2 = int(input("Enter next number: "))

    # above "function aaa" get called according to the choosen symbols
    calculation_function = operations[operation_symbol]

    first_answer = calculation_function(n1, n2)  # valued get passed to function

    print(first_answer)

    if input(f"Type 'y' to continue the calculation with {first_answer} or type 'n' to exit: ") == "y":
       n1 = first_answer

    else:
        should_continue = False #flag=false

