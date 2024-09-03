#password generator list + Random + loop
#control+shift+L for multiple cursor of same word
#shift + alt + click for multiple select
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password : \n"))
nr_symbols = int(input("How many symbols would you like : \n"))
nr_numbers = int(input("How many numbers would you like : "))

P = random.choice(letters)

#easy same type togather
#for string white space to occupy the value of variable "Password" but we use 0 incase of int
Password = " "

#nr_letter = 4 i.e. 1 to 4
for let in range(1, nr_letters + 1):#loop from 1 to 4 or 4 times and assign value to char each time
   
    random_char = random.choice(letters)#choose randomly from letters list

    #this print should be inside for loop else only print/add last letter
    Password += random_char


for sym in range(1, nr_symbols + 1):
   
    #directly
    Password += random.choice(symbols)


for num in range(1, nr_numbers + 1):
   
    

    Password += random.choice(numbers)

print(f"Your password is {Password}")


#########################################################################################33

#hard suffeed type i.e. using list
Password_list = []

for let in range(1, nr_letters + 1):
   
    random_char = random.choice(letters)

    Password_list.append(random_char)


for sym in range(1, nr_symbols + 1):
   
    Password_list.append(random.choice(symbols))


for num in range(1, nr_numbers + 1):
   
    

    Password_list.append(random.choice(numbers))

print(f"Your password is {Password_list}")#here we get in form of list
#still not shuffle

#goggle "how to change the order of item in a list python" we added keyword python to specifically find in python

#to shuffle we can use loop with new list

#or using suffle()

random.shuffle(Password_list)

print(Password_list)

#from list to string

password= ""
for passw in Password_list:
    password += passw
print(password)



