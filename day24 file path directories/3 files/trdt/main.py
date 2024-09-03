# #this only worked with when we are in direct folder "here in "trdt" 

# #to open file using bulit-in  "open()"" methode
# file = open("file.txt")

# #to read file using read()
# content = file.read()

# print(content)

# #to close the opened file (manually)
# file.close()
# #we need to close the file when we are done because it occupies resources of computer

############333333333333
#alternatively (with automatic close())
# with open("file.txt") as file:#no close() needed
#     content = file.read()
#     print(content)
    
# ######333333333
# #to write into that file
# with open("file.txt", mode="w") as file: #the "file.txt" is saved to variable call "file"
#     #by default mode="r" for other we need to mention
#     file.write("New text.")# this replace the content of file.txt to "New text."

# ############33333333
# #to add or append
# with open("file.txt", mode="a") as file:#mode = "a" for append 
#     file.write("\nNewer text.")# this append the content of file.txt to "New text."

# #when we try to open file which does not exist in write mode will create new file with that name
# with open("new_file", mode="w") as file:
#     file.write("new file has created hehe magic")

###########333333file path
# with open("/Users/Hp/Desktop/file for example of absolute file path day 24.txt") as file:#we need forward slash here no back-ward
#      content = file.read()
#      print(content)

#for relative path
#path of now this main.py (where we are now here  insider main.py now) is 
#"C:\Users\Hp\Desktop\programming\day 24\3 files\trdt\main.py"

#"C:\Users\Hp\Desktop\programming\day 24\file2.txt"

#making relative path with help of above path of "main.py" and file path of "file2.txt"

with open("..\..\file2.txt") as file:#we need forward slash here no back-ward
     content = file.read()
     print(content)

     