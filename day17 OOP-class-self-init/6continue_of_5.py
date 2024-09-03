class User:

    def __init__ (self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1#clear example of #################"self"



user1 = User("001", "angela")
user2 = User("002", "jact")

user1.follow(user2)#user1 follow user2


print(user1.followers)#still 0
print(user1.following)#got increase by 1/following 1 person

print(user2.followers)#got increase by 1/followed by 1 person
print(user2.following)#still 0
