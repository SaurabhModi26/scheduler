from django.http import response
from django.shortcuts import render,HttpResponse
from datetime import *
import requests
from home.models import APIData
from home import apitest



# Create your views here.
def index(request):
    
    # return HttpResponse("this is index page")
    # response=requests.get("https://api.covid19api.com/countries").json()

    # context={
    #     "variable":datetime.today(),
    #     "response":response,
    # }
    start_time=apitest.start_time
    event=apitest.event
    duration=apitest.duration
    timeleft=apitest.timeLeft
    # temp=sorted(context[response])
    # temp2={
    #     "variable":datetime.today(),
    #     "response":temp,
    # }
    # t=context[response].sort()
    # temp={
    #     "variable":datetime.today(),
    #     "response":t,
    # }
    # for i in range(1):
    #     value=APIData(
    #         start=start_time[i],
    #         dur=duration[i],
    #         timeleft=timeleft[i],
    #         event=event[i],
    #     )
    #     value.save()
    # data=APIData.objects.all()

    return render(request,"index.html",{"variable":datetime.today(),"start_time":start_time,"event":event,"duration":duration,"timeleft":timeleft})

def about(request):
    return HttpResponse("this is about page")