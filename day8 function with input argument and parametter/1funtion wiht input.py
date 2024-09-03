def greet():
    print("Hello")
    print('oh my oh!')
    print('Welcome')


greet()


# function that allows input

# here name is a variable "a cup" where we can fill and we called (here 'name') a parameter
def greet_with_input(name):
    print(f"Hello {name}")
    print(f'oh my oh! {name}')
    print(f'Welcome {name}')


greet_with_input("ram")  # the value we passed (here "ram") is called argument

# function with more than 1 input

# function positional argument
# because the argument "Ram" is assign to the parameter "name" autometically and same goes to "Kathmandu" to 'address"


def greet_with_positional_argument(name, address):
    print(f"Hi {name}")
    print(f"What is it like in {address}")


greet_with_positional_argument("Ram", "Kathmandu")

# problem in positional argument
greet_with_positional_argument("Kathmandu", "Ram")

#solution for above problem
# function with keyword argument
def greet_with_keyword_argument(address, name):
    print(f"Hi {name}")
    print(f"What is it like in {address}")

greet_with_keyword_argument(address='kathmandau', name="Rama")