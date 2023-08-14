from django.urls import path
from . import views

app_name= "main"


urlpatterns=[

    path("", views.first_page, name="home_view"),
    path("info/", views.info_page,name="info_view")
]