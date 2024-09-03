#how methode are created in class

#attribute are what object has 
#methode are what object does


class Car:

    def __init__ (self):
        self.seats = 5

    #remove seats to decrease weight of the vechile for racing
    def enter_race_mode(self, remove):#if we proceed from "__init__" funtion we need to add "self" parameter
                                      # as the 1st parameter to other function too, so that whenever that function get called it know the object that called it
        self.seats -= remove

my_car = Car()

print(my_car.seats)

my_car.enter_race_mode(3)

print(my_car.seats)