from django.urls import path 
from . import views

app_name ="my_first_app"

urlpatterns =[
    path("", views.Home_view, name= "Home_view"),
    path("info/", views.Info_view, name="Info_view")


]

