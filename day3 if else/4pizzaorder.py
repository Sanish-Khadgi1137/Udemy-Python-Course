print("Welcome to Pythn Pizza Deliverires!")
size=input("What size pizza do you want? s, m or l: ")

bill = 0
#there is mystrey bug in size choose solve it later
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

    add_pepperoni= input("Do you want pepperoni? y or n: ")
    if add_pepperoni == "y":
        if size == "s":
            bill += 2
        elif size == "m":
            bill += 3
        elif size == "l":
            bill += 4
    else:
        bill == bill

    extra_cheese = input("Do you want extra cheese? y or n: ")
    if extra_cheese == "y":
        bill += 1
    else:
        bill == bill

    print(f"Your final bill is ${bill}")


else:
    print("Invalid input")