from django.urls import path 
from . import views

name_app= "main"
urlpatterns = [
    path( '', views.home , name="home"),
    path('info/' ,views.info, name="car_info" ),
]
