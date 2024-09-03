# index error
fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]  # if find fruit in given index executes "else:"
    except:  # if entered index is out of range execute "except:"
        print("fruit pie")

    else:
        print(fruit + " pie")


make_pie(3)

# 33333333
# keyerror
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, "Shares": 1},
    {'Likes': 33, 'Comments': 2, "Shares": 1},
    {'Comments': 4, "Shares": 2},
    {'Comments': 2, "Shares": 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

# for post in facebook_posts:
#     total_likes = total_likes + post['Likes']

# #since very item in a list does not have key named "Likes"
# print(total_likes)

# solution
for post in facebook_posts:

    try:
        total_likes = total_likes + post['Likes']
    except:  # if encounter key-error just pass to new item in the list ; which add zero to the total_likes
        pass
        #or 
        #total_likes += 0


print(total_likes)
