#https://docs.python.org/3/library/turtle.html documentation for "Turtle Graphics"

import another_module #module(here can be said file name) imported 
print(another_module.another_variable) #printed "another_variable" from "another_module"

# import turtle
# timmy = turtle.Turtle()
#we create "object timmy" and tap into the "module turtle" and  we fetch "class Turtle()" from the imported module
#as above another_module(here "turtle") and another_variable(here class "Turtle()"")

#making above object "timmy" in more simpler way
from turtle import Turtle, Screen
#"Screen" is additional "class" impoted from "module turtle"

timmy = Turtle()
print(timmy)#this save the "brand-new Turtle-object "timmy" " from "turtle module" at this (eg. 0x00000167D00cf50) location of the computer memory /every run new location
timmy.shape("turtle")#on "method shape()" we defined shape of timmy to be turtle
timmy.color("coral")
timmy.forward(1000)

#above print is differet from below as it was object that being printed
# print("numbersss")

my_screen = Screen()#my_screen is object
print(my_screen.canvheight) #"canvheigh" is a property (attribute) of the "class Screen()"
#preceding print result a window pop-up very briefly(apper and diapper) and "canvas height" in console

my_screen.exitonclick()#clik on the diplay pop-uped to exit
#method "exitonclick()" called from object "my_screen"