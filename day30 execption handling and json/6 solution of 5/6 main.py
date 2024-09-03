#solution of 5
#if there was no such file updating json create     FILENOTFOUNDERROR
import json

website = input("Enter a website name: ")

eml = input("Email: ")
passw = input("Password: ")

json_data_f = {
    website:{
        "email": eml,
        "password": passw
    }
}



try:#read file
    with open("dataj1", "r") as data_json:
        jdata = json.load(data_json)

except FileNotFoundError:#if try(read) is not successful execute "except"
    with open ("dataj1", "w") as data_json:
        json.dump(json_data_f, data_json, indent= 4) 

else:#if trky(read) is sucessful update
    jdata.update(json_data_f)
    
    with open('dataj1', 'w') as data_json:
        json.dump(jdata, data_json, indent= 4)