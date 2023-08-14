from django.urls import path, include
from . import views

app_name = "rentalApp"

urlpatterns =[
    path('', views.helo_view, name="helo_view"),
    path('cars/', views.car_rental_page, name="car_rental_page"),
]