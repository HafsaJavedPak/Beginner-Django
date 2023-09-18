from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bye", views.bye, name="bye"),
    path("<str:name>", views.greet_everyone, name="greet_everyone"),
    
]