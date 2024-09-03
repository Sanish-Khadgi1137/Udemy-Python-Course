import requests #requests is need to be installed using "pip install requests"

#website url = http://open-notify.org/Open-Notify-API/ISS-Location-Now/
respond1 = requests.get(url="http://api.open-notify.org/iss-now.json")#internet connection is required to get data

print(respond1) # we god message <Response [200]>

data = respond1.json()#actually get data in json format

#if we only need is_position
#data = respond1.json()['iss_position']

#if we only need longitude of iss_position
#data = respond1.json()['iss_position']["longitude"]
#or 
longitude = data['iss_position']['longitude']

print(longitude)

print(data)

#status code url = https://www.webfx.com/web-development/glossary/http-status-codes/

respond1.raise_for_status() #this gives what was the status error we got

