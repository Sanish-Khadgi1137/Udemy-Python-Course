"""go to site "https://opentdb.com/api_config.php" and gereate link and in new
 tap use link and get data in json(javascript object notaion) format; copy and paste
 it below  'JSON extenstion by Meezilla" was installed for formating; and used
 by selecting only 'json data' and control+ship+j
 
 1. get rid of dictionary and make it list 
 2. and modify main.py with #we need @@@@@@@@@@@@@@ in place of text and answer
 """

#"response_code": 0,#1st key-value
    #2nd key-value
    #"results": 
question_data= [
    
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "RAM stands for Random Access Memory.",#we need@@@@@@@@@@@@@@@@
            "correct_answer": "True",#we need @@@@@@@@@@@@@@@@@@@@@@@@22
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "Linux was first created as an alternative to Windows XP.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "The Windows 7 operating system has six main editions.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "The logo for Snapchat is a Bell.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "Ada Lovelace is often considered the first computer programmer.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
            "correct_answer": "False",
            "incorrect_answers": [
                "True"
            ]
        },
        {
            "type": "boolean",
            "difficulty": "easy",
            "category": "Science: Computers",
            "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
            "correct_answer": "True",
            "incorrect_answers": [
                "False"
            ]
        }
]    