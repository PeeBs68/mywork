# https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m

# "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

import json
import requests
#url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m"
#url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m&current=wind_speed_10m"

#response = requests.get(url)
#data = response.json()
# Won't need this later so delete once everything is working
#with open ("json_dump.json", "w") as fp:
#    json.dump(data,fp)
# Use Alt + Shf + F to format the JSON file to be more readable
''''
current_temp = data["current"]["temperature_2m"]
#temp2 = temp["temperature_2m"]
print(f"The current temperature at Kinsale Golf Club is {current_temp} degrees celcius.")

url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=wind_speed_10m"
response = requests.get(url)
data = response.json()
current_ws = data["current"]["wind_speed_10m"]
print(f"The current wind speed at Kinsale Golf Club is {current_ws} kph.")
'''

url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m&current=wind_direction_10m"
response = requests.get(url)
data = response.json()
current_wdir = data["current"]["wind_direction_10m"]
current_temp = data["current"]["temperature_2m"]

# Just to add a bit more detail
if current_wdir < 90:
    wdir = "North/Easterly"
elif current_wdir < 180:
    wdir = "South/Easterly"
elif current_wdir < 279:
    wdir = "West/Southerly"
else:
    wdir = "North/Westerly"

print(f"Right now at Kinsale Golf Club the temperature is {current_temp} degrees celcius and the wind is blowing in the direction of {current_wdir} degrees (which is roughly {wdir})")
# https://open-meteo.com/en/docs/#current=wind_direction_10m&hourly=wind_direction_10m