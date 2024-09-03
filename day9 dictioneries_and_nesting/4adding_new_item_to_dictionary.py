#adding new entry/item/travel log to existing dicionary
#by making new dictionay with function way
travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "German",
    "visits": 5,
    "cities": ["Berlin", "Stuttgart", "Hamburg"]
}
]

#making funtion to add
def add_new_country(country_visited,times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited #these items are added to new dictionary "new_country"
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country) #this line add "new_country" dictionary to "travel_log" dictionary


#argument(Russia, 2, [Moscow,Saint Peterburg]) are passed for parameter(country_visited,times_visited,cities_visited) of funtion "add_new_country"
add_new_country("Russia",2,["Moscow","Saint Peterburg"])

print(travel_log)