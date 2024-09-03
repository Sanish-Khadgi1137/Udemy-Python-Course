print(8/3)

print(int(8/3))

#round() is used to round the number
print(round(8/3))
# is 2.66666666665 which is near to 3 so rounding gives 3 as answer

#here ,4 indicate rounding that number upto 4 decimal places
print(round(8/3,4))
print(round(2.77777777777,4))

# "//" this way of division gives integer output not float
print(8//3)

# shorthand operators
score = 100
score +=10

print(score)

#mixing string and different datatypes

result = 33
height = 1.85
isWining = True


print("your result is " + str(result))

#instead we can use "F-String"
print(f"your result is: {result}, your height is: {height} , your are wining:{isWining}")
