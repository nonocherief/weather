from datetime import datetime
import requests

res = requests.get("https://api.open-meteo.com/v1/forecast?latitude=48.2092&longitude=16.3728&hourly=temperature_2m,precipitation,windspeed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum,precipitation_hours&timezone=Europe%2FBerlin")
#res = requests.get("https://www.google.com/")
#print(res.text)
#print(r.json())

data = res.json()

i=0
while i<len(data["hourly"]["time"]):
    print(data["hourly"]["time"][i])
    print(data["hourly"]["temperature_2m"][i])
    i=i+1

def goodforrunning(l1):
    x=True
    for i in l1:
        if i<10:
            x=False
    return x

print(goodforrunning(data["hourly"]["temperature_2m"][0:24]))

def time(l2):
    b=0
    for c in range(7):
        a=b
        b=b+24
        print(l2["time"][a])
        print(goodforrunning(l2["temperature_2m"][a:b]))

time(data["hourly"])





