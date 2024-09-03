print("You're welcome to Tresure Island")

print('Your mission is to find the tresure.')

#back-space(\) before single-quotation(') enable us to write single-quotation(') to make "you are" to "you're"
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right": ')

#logical error like choice1 == "left" or "Left" could create logical error/bug
if choice1 == "left" or  choice1 == "Left": 
    #if user input capital letter of small letter ("left" or "Left") make pc to treat same or we can you .lower() as in below

    #if we have to use double-coated ("") word inside string use single-quotation('') for string in input
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for the boat or "swim" to swim across: ').lower()
    #lower() make all input to smaller letter which make pc to treat both "right" and "Right" as same

    if choice2 == "wait":

        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you chose: ").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You've found the tresure. You Win!")
        elif choice3 == "yellow":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doen't exist. Game Over.")
    
    else:
        print("You got attacked by an angry trout. Game over!")    

else:
    print("Game over! You've fell into the whole.")