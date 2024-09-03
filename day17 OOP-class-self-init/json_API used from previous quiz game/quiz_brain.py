# bring up the question bank and ask the user
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0  # initial question number is 0 due to indexting in list
        self.question_list = q_list  # list of question in question_bank in main.py
        self.score = 0

    def still_has_questions(self):
        """keep asking if there is question remaining"""

        """
        if self.question_number < len(self.question_list):
            return True
        else:
            False
        """
        # more simpler form; computer evaluate expression below and give in true if correct else false
        return self.question_number < len(self.question_list)

    def next_question(self):  # if this line is intended inside the above methode it also execute while calling the class; and while calling this method get error saying "AttributeError: 'QuizBrain' object has no attribute 'next_question'"
        """Retrieve the item at the current question_number from the question_lists. Use the input() function to show the user the Question text and ask for the user's answer"""
        current_question = self.question_list[self.question_number]  # "self.question_number" is current question number in question bank "self.question_list"

        self.question_number += 1  # due to list index 1st question number is 0 if we dont do this; after/ once we've gotten hold of the current number; tap into that current number and increase it by 1

        # "self.question_number" give current question number and "current_question.text" gives question
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # correct_answer = current.question.answer
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You go it right!")
            # (tracked) if correct answer the self.score gets increased by 1
            self.score += 1
        else:
            print("That's wrong.")
        # this is out of the if/else so print this statement for both cases
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
