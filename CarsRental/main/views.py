from django.shortcuts import render
from django.http import HttpRequest ,HttpResponse
# Create your views here.

def home_view(request: HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here.\n "
    return HttpResponse(content)

def car_viwe(request: HttpRequest):

    content = "<h2 style='color:green'>Asimple paragraph about Car Rentals.</h2>"

    return HttpResponse(content)