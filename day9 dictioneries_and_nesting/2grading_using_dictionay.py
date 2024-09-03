#grading program using dictionary converting marks to grade
#new dictionary linked with old dictionary
student_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grade = {}

for student in student_score:
#here for loop go through each of keys only
#for checking
   #print(student) 
   score = student_score[student]
   #score assign to score of student looped from dictionay student_score
   if score > 90:
        student_grade[student] = "Outstandign"#here [student] is that key at that instant of time
   elif score > 80:
        student_grade[student] = "Exceeds Expecttaion"
   elif score > 70:
        student_grade[student] = "Acceptable"
   else:
        student_grade[student] = "Fail"
     
print(student_grade)