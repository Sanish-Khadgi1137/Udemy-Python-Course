#able to describe a problem is you have already got solution


#print every line as much as possible and check if it working correctly
"""###########################333333
#describe Problem
def my_function():
    for i in range(1, 21):#range was from (1, 20) but it will loop from 1 to 19 only but the  condition was i == 20 /solution make range(1, 21)
        if i == 20:
            print("You got it")

my_function()#function called
"""



"""#######################
#reproducing the bug; bug that come only some time /there types of bug is really difficult
from random import randint

dice_imgs = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"] #even parenthesis worked here
dice_num = randint(0, 5)  #list start from 0 to n-1 but here randint(1,6) so there is no dice for 6 because n-1/test by puting all number of range eg(dice_num = 6) and do from 0/1 to 6 test which gives error /solution make it (0, 5)
print(dice_imgs[dice_num])

"""




"""##################################333333
#play computer trie to read like a computer not human
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial")
elif year > 1994:
    print("You are a Gen Z.")
"""
"""we will encounter bug(print nothing) while we in put 1998 or 1994 
because computer for (1994) reads lesser than 1994 in 1st condition and greater than in 2nd condition

solution is making 1st condition "year >= 1980 and year <= 1994" from "year > 1980 and year < 1994"
"""#triple colons comment inside triple comment do not work


"""##############################333
#fix the error when console or editor (red underline) giving error fix it first
#search the error in goggle or stack overflow

age = input("How old are you?")#int vs string error show on console while run
if age > 18:
print("You can drive at age {age}.")#indentation error show by red line in editor
#and f-sting error this error is furstrating as not showing error but not working as we want /need to rely on skill and experience comes in really handy with debugging
"""


"""############################3
#print is your friend
pages = 0 #pages start at 0
word_per_page = 0 #word_per_page start at 0

pages = int(input('Number of pages: '))
word_per_page = int(input('Number of words per page: '))# "==" is eqaul to and "=" is assinging
#from friend"print" we spot problem in this line it was making "0" even input was not 0
# solution is ma "=" from "==" 
total_words = pages * word_per_page

#using your friend print to test
#print(f"pages = {pages}")
#print(f"word_per_page ={word_per_page}")

print(total_words)
"""


#use a debugger  such as thonny, pythontutor.com
def mutate(a_list):
    b_list = []#created empyt b_list
    for item in a_list:
        new_item = item *2
    b_list.append(new_item)#new item is added to b_list
    #write above line so that for each item in loop get append to list b otherwise only last item get stored
    #it was running only once at end but after correction it run 6 times along with loop
    print(b_list)

#fuction call and passed list argument
mutate([1, 2, 3, 5, 8, 13])

#use https://pythontutor.com/render.html#mode=display to see step by step excution
#from step by step we found in appending to b_list see above


#7 take a break and see with different fresh view
#8 ask a human friend we could make different assumption(fresh eye) than you did
#9 run the code ofen / check step by step as you proceed do not wait to complete whole program / ton of bug is hectic than few(you wont know where to start)
#10 go stackoverflow or chatgpc if not found then go oracle or community

#11 if we make changes see what other changes is needed if i change that