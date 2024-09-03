number=int(input("Enter a number:\t"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#ternary operator/expression instead of if-else statement makes code concise but decrease readiablity so not good for professional practise 
a=int(input("Enter a number"))
b=int(input("Enter second number"))

min= a if a<b else b

print(f"the minimun number is {min}")