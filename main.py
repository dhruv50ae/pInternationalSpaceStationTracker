import requests
from datetime import datetime

NOT_MY_LAT = 51.510357
NOT_MY_LNG = -0.116773

parameters = {
    "lat": NOT_MY_LAT,
    "lng": NOT_MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

timeNow = datetime.now()

print(timeNow.hour)
