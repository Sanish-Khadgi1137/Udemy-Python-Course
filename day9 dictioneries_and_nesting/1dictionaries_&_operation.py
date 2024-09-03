#Dictioneries and operation on dictionary
#dictionneray name = { "key": "value"}
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
"Funtion": "A piece of code that yu can easily call over and over again.",
123: "numbers."}

#proper format (ease readable) "{" enter, "1 indentation", "next item" and "}"
x_dictionary = {
 "A": "a for apple",
 "B": "b for ball"    
}

#retrving or feteching from dictionary
print(programming_dictionary["Bug"])
#use key in same as in dictionary else give keyerror

print(programming_dictionary[123])

#adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

#its preety helpful to start off with empty dictionary
#creating empty dictionary
empty_dictionary = {}

print(x_dictionary)
#empty dictionary also can be use to clear/wipe existing dictionary eg
x_dictionary = {}

print(x_dictionary)

#edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)#this print only keys
    print(programming_dictionary[key])#this print value for each key


programming_dictionary.keys()