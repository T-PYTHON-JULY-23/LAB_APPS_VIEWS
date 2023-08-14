from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("",views.car_viwe, name= "car_viwe"),
    path("info/", views.cars_view, name= "car_viwes"),
]