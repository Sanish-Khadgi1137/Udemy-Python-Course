# we used recursive function which "calls itself"

#while we exit from current calculation recursive function take to new state (here)

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

def calculator(): #recursive function; it takes no input and give no output

    n1 = float(input("Enter first number: ")) #use float() to take decimal points too

    for symbol in operations:  # loops through the operations dictionary
        print(symbol)

    should_continue = True  # "should_continue" flag

    while should_continue: #while flag is true ; here not specified means true

        operation_symbol = input("Pick a operation: ")

        n2 = float(input("Enter next number: "))

        # above "function aaa" get called according to the choosen symbols
        calculation_function = operations[operation_symbol]

        first_answer = calculation_function(n1, n2)  # valued get passed to function

        print(first_answer)

        if input(f"Type 'y' to continue the calculation with {first_answer} or type 'n' for new calculation: ") == "y":
           n1 = first_answer

        else:
            should_continue = False #flag=false

            calculator() #recursive function calling itself




calculator()#function call



# #should not do in recursive function because it looping for every (infinite loop)
# def calcualtor():
#     print("sssssssssss")
#     calcualtor()

# calcualtor()
