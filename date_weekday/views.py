from django.shortcuts import render
from django.http import HttpResponse
import datetime

now = datetime.datetime.now()
isit_even_day = (now.day)%2
# Create your views here.
def index(request):
    return render(request, "date_weekday/index.html", {
        "even_ornot" : isit_even_day, "weekday": now.strftime("%A"), "date": now.day, "day" : now        
    })    