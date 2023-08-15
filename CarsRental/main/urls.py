from django.urls import path
from . import views


app_name="main"

urlpatterns = [
    path("", views.car_rentals_home, name="home_view"),
    path("info/", views.car_info, name="welcome_view")]

