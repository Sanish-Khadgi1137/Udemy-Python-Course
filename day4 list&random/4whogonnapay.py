import random

names_string = input("Give me everybody's names, seperated by a comma. ")

#to splits elements on the basis of a comma and a white space (", ")
names = names_string.split(", ")
#and save to list

#print(names[2])
'''
num_items = len(names)



random_ch = random.randint(0, num_items-1)

pay = names[random_ch]
'''

#this choice() function can do work of above 3 lines alone
pay = random.choice(names)

print(pay + " going to by the meal today")