from django.urls import path
from . import views

app_name = "CarsRental"
urlpatterns = [
path("path/", views.Movie_Name, name="path")
]


