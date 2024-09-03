student_heights = input("Input a list of student heights: ").split()
#split() save the input in a list seperated by comma 
#white spaces in input is considered as speration


#stu[n]= int(student_heights[n])
#above way of making input is not applicable for list so use loops as below
for n in range(0, len(student_heights)):
   student_heights[n] = int(student_heights[n])

print(student_heights)
'''
not using these 2 cheat sheet function
#if not splited len() will count every single digits and whitespaces
print(len(student_heights))
print(sum(student_heights))
'''
total_height=0

for height in student_heights:
    total_height += height
    #if the print(total_height) was here inside a loop it print result of every instance of sum result from 1st to last
#print outside of loop gives final sum    
print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

average_height = round(total_height / number_of_students)

print(average_height)