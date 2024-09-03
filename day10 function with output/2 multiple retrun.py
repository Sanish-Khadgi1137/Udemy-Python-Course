def format_name(f_name, l_name):

    if f_name =="" or l_name =="":
        #return #returning empty function ;which is not good so
        return "Invalid inpput"
    
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()

    return f"{formated_f_name} {formated_l_name}"

    print("hello")# this won't get executed because it is after "retrun", return means end of the function

print(format_name(input("first name"),input("Last name")))

dfsdffsdf