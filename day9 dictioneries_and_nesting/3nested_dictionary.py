#nested dictionary
"""
in dictionay one "key" can not have multiple values in normal condition
for example= 

travel_log = {
    "france": "Lille", "Paris", "Dijon"
}

"""
#for it we can use nested dictionary (dictionary inside dictionary) or list inside dictionary
travel_log1 = {
    'German': ["Hamburg", "Stuttgart", "Berlin"],#do not forget comma here
    "France": {"Cities_visited": ["Lille", "Paris", "Dijon"], "Total_visit":12}#list inside dictionary inside dictionary
}

#Nesting Dictionary in a list

travel_log2 = [
    {
        "country":"France",
        "cities_visited": ["Paris", "Lille", 'Dijon'],
        "total_visits": 12
    },
    {
        "country": "German",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visited": 5

    }
    ]

print(travel_log2)