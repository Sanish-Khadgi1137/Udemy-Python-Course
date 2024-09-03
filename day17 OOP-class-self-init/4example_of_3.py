class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.follower = 0 #initail value which later get modified no need to pass argument when object called
        self.username = username
#we can pass the argument in time of object creation
user_1 = User("001", "angela")

print(user_1.username)

print(user_1.follower)

"""
#this give error as there is need to pass argument while calling due to inti function has passed parameters
user_2 = User()

user_2.id = " 002"
user_2.username = "jack"
"""