import requests

# sun_respose = requests.get('https://api.sunrise-sunset.org/json')
# sun_respose.raise_for_status()#to raise error status for other than 200(successful)

# sun_data = sun_respose.json()

# print(sun_data)
#these result 404 error as  request is  not propor (in which location do we want time of sun raise and set)

#https://www.latlong.net/

MY_LAT = 27.717245
MY_LONG = 85.323959

parameters = {
    "lat" : MY_LAT,
    'lng' : MY_LONG,
    "formatted" : 0 #mean 0 = off which give time in 12 hours format
}
                        #this link is called end point
sun_respose = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
sun_respose.raise_for_status()#to raise error status for other than 200(successful)

sun_data = sun_respose.json()

               #result is most outer dictionary of data we got
rise = sun_data['results']['sunrise']
set = sun_data["results"]['sunset']

print(rise)
print(rise.split('T'))
print(rise.split("T")[1].split(':')) #split second part further
print(rise.split("T")[1].split(':')[0])#to get only hour
#print(sun_data)

