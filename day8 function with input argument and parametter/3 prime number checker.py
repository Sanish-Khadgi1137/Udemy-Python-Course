#prime number(only divisible by itself or 1) checker

#print also get looped so lots of answer
def prime_checker(number):
    for i in range(2, number): #from 2 to just less then "number"
        if number % i == 0:
            print("is not prime")
        else:
            print("prime")

number = int(input("Enter the number"))

prime_checker(number)

# #solution for above
# def prime_checker(number):
#     is_prime=True
#     for i in range(2, number): #from 2 to just less then "number"
#         if number % i == 0:
#             is_prime=False
        
#     if is_prime: # this expression  is same as is_prime = True
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")

# number = int(input("Enter the number"))

# prime_checker(number)