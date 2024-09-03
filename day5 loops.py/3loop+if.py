student_scores = input("Enter a list of student scores").split()
for n in range(0, len(student_scores)):
    #[n] is a variable assign to each element simultaneously and point in list below
    student_scores[n] = int(student_scores[n])

print(max(student_scores))
print(min(student_scores))

highest_score = 0

#here "score" is single score form a list "student_scores"
for score in student_scores:
    if score > highest_score:
        highest_score= score

print(f"The highest score is {score}")