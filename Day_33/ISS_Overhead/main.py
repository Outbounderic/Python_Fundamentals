import requests
from datetime import datetime

MY_LAT = 32.776665
MY_LNG = -96.796989

params = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

time_now = datetime.now()
print(f"{sunrise} : {sunset} : {time_now.hour}")