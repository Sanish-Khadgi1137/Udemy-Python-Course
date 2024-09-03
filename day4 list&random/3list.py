#https://docs.python.org/3/tutorial/datastructures.html
states_of_america = ["Delaware","Pennsylvania","New jersey", "Georgia","North Dakota","Minnesota","Arizona"]

#offset/shift 0 gives first element of the list
print(states_of_america[0])

# -1 gives last element and -2 gives second last and so on.
print(states_of_america[-1])

#to replace values of offset 1
states_of_america[1] = "Pencilvania"

#to add new single element at last to the list
states_of_america.append("kathmandu")

# to add multiple element
states_of_america.extend(["doha", "Pokhara", "Moscow"])

print(states_of_america)

#this gives index error because we tried to display element of with index "50" which is does not exist
print(states_of_america[50])


