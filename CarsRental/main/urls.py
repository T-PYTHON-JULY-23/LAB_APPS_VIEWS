from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.car_view , name = "car_view"),
    path("info/", views.cars_view , name="cars_view"),

]
