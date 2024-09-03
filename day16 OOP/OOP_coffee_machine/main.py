from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu1=Menu()
money_machine1 = MoneyMachine()#object created" money_machine1"
coffee_maker1 = CoffeeMaker()

is_on = True #coffee machine is on

while is_on:
    option = menu1.get_items() #to get what's on menu
    choice = input(f"What would you like? ({option}):")#taking order from the customer
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker1.report()
        money_machine1.report()
    else:
        drink = menu1.find_drink(choice)#oder name
        if coffee_maker1.is_resource_sufficient(drink):#check for resources for choosen drink
            if money_machine1.make_payment(drink.cost):#check if money is sufficient
                coffee_maker1.make_coffee(drink)#makes coffee

'''
#in output 
1. "report" for to get info about resources available and money
2. "off" to switch off the machine and exit the code
3. latte/cappuccino/espresso create object and save to memory
'''


"""__pycache__ is a directory that is created by the Python interpreter when 
it imports a module. It contains the compiled bytecode of the
 module, which can be used to speed up subsequent imports of the same module."""