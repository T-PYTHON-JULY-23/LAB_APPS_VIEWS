from django.urls import path
from . import views

app_name="mainCarsRental"

urlpatterns = [
    path('',views.view_welcome, name="view_hello"),
    path('info/',views.carsrental, name="cars rental")
]