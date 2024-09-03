# only worded when we open vs code directly with "5 Mail merge project(carbon copy)"


PLACEHOLDER = "[name]"

# with open("./Input/Names/invited_names.txt") as names_file:
# also so we can use "path" in shorter formate below without "./"
with open("Input/Names/invited_names.txt") as names_file:

    # names = names_file.read() #normal read
    # readlines convert string in the file to list format
    names = names_file.readlines() #these list of names has new_line i.e. /n we use strip to remove it
    # print(names)

with open("Input\Letters\starting_letter.txt") as letter_file:
    # normal read = display file as it is in .txt file
    letter_content = letter_file.read()
    # print(letter_content)
    for name in names:
        
        striped_name = name.strip() #inbuilt strip() method strip/delete/take away white_spaces or new_line i.e. '/n'
        
        #to replace there should be string not list here "PLACEHOLDER"
        new_letter = letter_content.replace(PLACEHOLDER, striped_name) #replace() inbuilt methode replace content here in starting_letter.txt 
        #print(new_letter)

        #this auto create letter for all
        with open(f"Output/ReadyToSend/Letter_for_{striped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
