class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {   #dictionary
            "water" : 300,
            "milk": 200,
            "coffee": 100
        }

 
    def report(self):
        """Prints a report of all resources."""

        print(f"Water:{self.resources['water']} ml") #['water'] fetching from dictionary
        
        print(f"Milk:{self.resources['milk']} ml")
        
        print(f"Coffee:{self.resources['coffee']} ml")


    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        
        can_make = True
        
        for item in drink.ingredients:
            
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False

        return can_make

  
    def make_coffee(self, order):
        """Deducts the required ingredients fromt the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
            print(f"Here is your {order.name} ☕️. Enjoy!")





#to check if there's any error just run it if no problem is show its good to proceed