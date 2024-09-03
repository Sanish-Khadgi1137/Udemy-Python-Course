"""
try: use to execute some things(some thing that might cause execption)

except: execute if "try:" encounter a error or there is an exeception

else: execute if there was no exeception

finnaly: do this no matter whatever happens
"""

##############333333333333333333
#FileNotFoundError

try:
    file= open("a_file.txt")#this file is not exist so error occurs are "except" gets executed
except:
    #print("There was an error")
    file= open("a_file.txt", "w")# if try: gives error (FileNotFoundError) here this execption create tha file
    file.write("someting")

#########3333333
#execpt: execute only if first condition produce error and ignore others if there are many task/lines

# try:
#     file = open("a_file.txt") #this execute as there is this file but
    
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sfssf"])# -this create keyerror as there is no such key "sfssf" in the dictionary

# except: #even there was error in second task except can not track/handle the error in this case
#     file = open("a_file.txt")
#     file.write("abcdefu")


###########333333333333333
#solution for above "except" not handling error
#we must make exception to catch specific situation eg.
try:
    file = open("a_file.txt")
    
    a_dictionary = {"key": "value"}
    print(a_dictionary["sfssf"])

except FileNotFoundError: #this exception handle only filenotfound error and in this condition we encounter "keyerror"
    file = open("a_file.txt")
    file.write("abcdefu")

# except KeyError: #if we use this too; this line handles keyerror 
#     print("That key doesnot exist")

#or
except KeyError as error_messafe: #also to hold error message
    print(f"The key {error_messafe} does not exist")

else: #else only get executed only if all line of "try" gets execute successfully
    content = file.read()#to make execute this we must give valid key that is "key" to print() in "try"
    print(content)

finally:#this execute regardless of execution result of "try" /finally is not oftenly used
    file.close()
    print("The file was closed")