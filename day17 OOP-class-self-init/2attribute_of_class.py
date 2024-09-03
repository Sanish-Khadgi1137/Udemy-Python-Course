#working of the attribute

class User:
    pass

user_1 = User()

user_1.id = "001"#"id" is atrribute of object user_1 created from class User()

#we can write as many atribut as we want
user_1.username = "Rikishi" 

print(user_1.username)

print(user_1.id)

#2nd object
user_2 = User()

user_2.id = "002"
user_2.username = "sumnima"

print(user_2.username)

