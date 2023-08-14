from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def car_view(Request : HttpRequest):
    contect = "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    return HttpResponse(contect)


def cars_view(request: HttpRequest):
     content = "A simple paragraph about Car Rentals."
     return HttpResponse(content)


# Create your views here.
