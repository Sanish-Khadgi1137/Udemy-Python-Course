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

# #to write data
# #with open("dataj1.json", "w") as data_json: 
# #or
#           #"dataj1.json" file will be created
# with open ("dataj1", "w") as data_json:#this create new .json file
#     #json.dump serialized python-data to json-data
#     json.dump(json_data_f, data_json, indent= 4) #indent will arrange json data from "line if not intent added" to indented order form
#     # intent = 4 means 4 spaces = 1 tab
#     print(type(data_json))
# #created file gets save to most outter folder but if there is file with same name here(json_data_f)
# # -but empty file; when we create with above command in this case(already existed file with same name) get overwrite to that existing file

# ##########3333333
# #to read data
# with open("dataj1", "r") as data_json:
#     jdata=json.load(data_json)# we used json.load to deserialized json-data to python-data

#     print(jdata)
#     print(type(jdata))#type = dicts
 

 ###############333333333
#to update ; update != append
with open("dataj1", "r") as data_json:
    #1 Reading old data
    jdata = json.load(data_json)

    #2 Updating old-data with new-data
    jdata.update(json_data_f)
    #see

with open('dataj1', 'w') as data_json:
    #3 Saving updated data
    json.dump(jdata, data_json, indent= 4)
              #see
#this result update of data = new data added inside dictionary

#if we try to update data/ run this code when there is no such file exist here "json_data_f"