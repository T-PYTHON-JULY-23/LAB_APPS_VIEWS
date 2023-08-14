from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

def car_viwe(Request : HttpRequest):
    contect = "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    return HttpResponse(contect)

def cars_view(Request : HttpRequest):
    contect = "A simple paragraph about Car Rentals."
    return HttpResponse(contect)
# Create your views here.
