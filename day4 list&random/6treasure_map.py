#sorting in map or nested list
row1 = ["a ", "b ", "c "]
row2 = ["d ", "e ", "f "]
row3 = ["g ", "h ", "i "]

#nested list
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

#event typed number this treate input as string
position= input("Where do you want to put the tresure?")

#we used int() where as inputed value was string
horizontal = int(position[0]) #this is offset "0" of the input 
vertical = int(position[1]) #this is offset "1" of the input

'''
#selecting row (column)
selected_row = map[vertical-1]

#in above selected row at horizontal position replay by "X"
selected_row[horizontal-1] = "X"
#(row)
'''
#or in single line
map[vertical-1][horizontal-1] = "@"

print(f"{row1}\n{row2}\n{row3}")