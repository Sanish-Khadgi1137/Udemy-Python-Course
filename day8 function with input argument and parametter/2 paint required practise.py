#number of cans of paint required to paint a wall
import math #to use math.ceil() for ronder to upper value

def paint_calc(height, width, cover):
    area=height*width
    no_of_cans= math.ceil(area/cover)
    print(f"you will need {no_of_cans} cans of paint")

test_h=int(input("Enter the height of the wall"))
test_w = int(input("Enter the width of the wall"))
coverage = 5

paint_calc(height=test_h, cover=coverage, width=test_w)