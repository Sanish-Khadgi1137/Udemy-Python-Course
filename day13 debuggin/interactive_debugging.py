"""
number = int(input("Which number do you want to check? :"))

if number % 2 = 0:# make is eqauls to (2bit operator) from "=" 1 bit assinging operator
    print("This is an even number.")
else:
    print("This is an odd number.")
"""



"""################################
year = input("Which year do you want to check")


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")    
else:
    print("Not a leap year")    

#error because opation between variable of different data types
#gives error "TypeError: not all arguments converted during string formatting"
#solution make input type to int
"""



for number in range(1, 101):

    print(f"Currently on number: {number}")

    if number % 3 == 0 or number % 5 == 0:#"or" check if one condition is true then whole is ture. So; it was displaying "Fizz" as well as "FizzBuzz" for number divisible by 3 and "Buzz" and "FizzBuzz" for number divisible by 5make it "and"
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number])
        """
        # to discard list in answer do print(number) only no []
        #above print(number) printing number for all but it was suppose to 
        not print number for number which is divisible by 3 or 5 or both 
        supposed to print "Fizz", "Buzz" or "FizzBuzz" only
        #after "or" corrected to "and" it was supposed to print number if 
        only all the condition was false
        # only if divisible by 5 number was not printed so else worked for 
         last if statement only 
        # what happend was it goes through all condition even else too except
        for divisible by 5 (divisible by 5 didnt went to else so only Buzz for it) use pythontutor.com to check 
        #because of if every-where
        #solution is use "elif" in 2 middle "if statements" what elif does is if the condition get "True" 
        direct print and skip other condition
        """


#corrected
for number in range(1, 101):

    print(f"Currently on number: {number}")

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        