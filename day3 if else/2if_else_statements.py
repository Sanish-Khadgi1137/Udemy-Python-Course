print("Welcome to the rollercoaster!")
height=int(input("How tall are you (in cm)?\n"))

if height >= 120:
    print("You can ride rollercoaster!")
    #2 nested if else(if inside if)
    age= int(input("How old are you?\t"))
    if age < 12:
        bill = 4
        print("Please pay $4.")
    elif age <15: #"> 12 & age < 16:" no need to write in range as about case is below 12 and this case is below 16 python automatically reconize it unlike in c++
        bill = 4
        print("Please pay $5")
    elif age <=18:
        bill = 7
        print("Please pay $7")
    #4 logical operators "and"    
    elif age >= 45 and age <= 55:
        print("Everythings is gonna be okay, Have a free ride on us!")
        bill = 0
    #4free ride for midlife crisis people
    else:
        bill = 10
        print("Please pay $10")
    #3 multiple if statements in succession(multiple checking i.e. multiple if in same indentation level)
    want_photo=input("Do you want a photo taken? y or n. ")
    if want_photo == "y":
        bill+= 3
        print(f"Your bill is ${bill}")

#2
else:
    print("Sorry, you have to grow up before you can ride rollercoaster")
