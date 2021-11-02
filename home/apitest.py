import json
import requests
from datetime import *

def bubbleSort(arr,duration,event,start_time):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                duration[j], duration[j+1] = duration[j+1], duration[j]
                event[j], event[j+1] = event[j+1], event[j]
                start_time[j], start_time[j+1] = start_time[j+1], start_time[j]


resp=requests.get("https://codeforces.com/api/contest.list").json()


start_time=[]
duration=[]
timeLeft=[]
event=[]

# print(resp['result'])
for i in range(len(resp["result"])):
    event.append(str(resp["result"][i]["name"]))
#start time
for i in range(len(resp["result"])):
    # start_time.append(str(datetime.fromtimestamp(resp["result"][i]["startTimeSeconds"]).strftime(" %d, %Y %I:%M:%S")))
    start_time.append(((resp["result"][i]["startTimeSeconds"])))


#duration
for i in range(len(resp["result"])):
    # duration.append(str(timedelta(seconds=resp["result"][i]["durationSeconds"])))
    duration.append(resp["result"][i]["durationSeconds"])

#timeLeft
for i in range(len(resp["result"])):
    # then=datetime.fromtimestamp(resp["result"][i]["startTimeSeconds"])
    # now=datetime.now()
    then=resp["result"][i]["startTimeSeconds"]
    now1=datetime.now()
    n=datetime.timestamp(now1)
    timeLeft.append((then-n))


# print(str(timedelta((then-now).total_seconds())))

# print(resp["result"][0]["name"])
# print(resp["result"][1]["phase"])
# print(resp["result"][1]["name"])


# resp2=requests.get("https://clist.by/api/v2/contest//?username=Pranav&api_key=d3cc1b52233c62834e8919f8411f0799707c1a98").json()


bubbleSort(timeLeft,duration,event,start_time)
i=0
while(timeLeft[i]<0): i=i+1

timeLeft=timeLeft[i:]
duration=duration[i:]
event=event[i:]
start_time=start_time[i:]

for i in range(len(timeLeft)):
    timeLeft[i]=((timedelta(seconds=timeLeft[i])))
    duration[i]=((timedelta(seconds=duration[i])))
    start_time[i]=datetime.fromtimestamp(start_time[i])
