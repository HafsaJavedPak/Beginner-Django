from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "helloWorld/index.html")

def greet_everyone(request, name):
    return render(request, "helloWorld/greet.html", {"name" : name.title()})

def bye(request):
    return HttpResponse("Goodbye! 👋🏻🤍")