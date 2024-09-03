print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
naem2 = input("What is your partner's name? \n")

#concatination no addition
combined_string = name1 + naem2
lower_case_string = combined_string.lower()

#count("a") is to used to count frequency of t in lower_case_string 
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

#changing int to str and concatinate then chaging love_score back to int for comparing wiht int in if-else
love_score = int(str(true) + str(love))


# () or () these brakets are but required but it improve readability for human
if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright togather")
else:
    print(f"Your score is {love_score}")
print(love_score)