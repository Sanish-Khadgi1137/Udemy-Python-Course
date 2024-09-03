from question_model import Question
from data import question_data

from quiz_brain import QuizBrain


#creating question bank
question_bank = []#empty list

for question in question_data:#loop in list of question in "data.py" file
    question_text = question["text"]#variable "question_text" comes from dictionary in data.py
    question_answer = question["answer"]#from daya.py save to "question_answer" which have "answer" key

    #creating new_question object
    #new_question = Question(q_text=question_text, q_answer=question_answer)#named parameter
    new_question = Question(question_text, question_answer)#positional parameter

    question_bank.append(new_question)#adding each "new_question" in question bank created in for loop

#print(question_bank)#this goes through question_data using for loop and add each to question_bank inside a list
#and save to computer memory

#print(question_bank[0].text)
 
#creating question bank

#askig the user
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():#check if the quiz still have question and run next_question again else exit the quiz
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")