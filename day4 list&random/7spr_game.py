#scissor paper rock
#https://devdojo.com/kmhmubin/build-a-python3-rock-paper-scissor-game-using-ascii-art
#https://wrpsa.com

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''                                                   

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor."))

import random
#if you write a code with ramdomint() at first execution it gives random number as last case you type which make easy to test that code
#eg. if check random_integer < user_input    in (0, 2) 
# print(you lose)
# if user inputed 1; randomint() gives 0
#which enable testing
computer_choice = random.randint(0, 2)

print(f"Computer chose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You wins!")
if computer_choice == 0 and user_choice == 2:
    print("Computer win!")          
elif computer_choice > user_choice:
    print("Computer wins!")  
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("Draw!")   
else:
    print("You chose invalid!")                                                                                   
                                                                                        
