# init function and self attributes
"""
how can i specify starting pieces of information(id, username) when i create object from a class
in order to do this(specify) we should understand 

constructor= what should happen when our object is being constructed
to create constructor in python is by using special function(i.e. init fuction)

def __init__(self)
#normally use to initialise attributes = creating initial/starting values for attribute

initialize = to set (variables, switches, counters, etc.) to their starting values as the beginning of a program or subprogram


@@@1@@@ init function is going to be called everytime you create a new object from that class
"""

class User:
    def __init__(self):
        print("new user being created...")#@@@1@@@ proof of called init function

user1=User()#when this construction happens/create a new user @@@1@@@ statements happens

user1.username="yuri"

print(user1.username)#@@@1@@@

user2=User()


#setting attributes in constructor
class Car:
    def __init__(self, seats):#self is actual object being created
        self.seats = seats
        #seats parameter pass in when a object is created from the class
"""
    if mycar = object(self) "mycar.seats = Car(seats)

       mycar = Car(5)

        which is actually

        mycar.seats = 5
     """