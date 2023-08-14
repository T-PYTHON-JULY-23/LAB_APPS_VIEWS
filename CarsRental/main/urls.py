from django.urls import path
from .import views


app_name ="main"


urlpatterns = [
    path(" " , views.home_view ,name="home_view" ),
     path("" , views.car_viwe , name ="car_view")
]



