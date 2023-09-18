from django.urls import path
from . import views

app_name = "date_weekday"
urlpatterns = [
    path("", views.index, name="index")
]