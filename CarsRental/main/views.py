from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def home(reques:HttpRequest) -> HttpResponse:
    content="<h1> Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    return HttpResponse(content)


def inf(request:HttpRequest) -> HttpResponse:

    content="<p> CarRental informtion where you find a car and rent it the store has been bulid since 1999 and it first started in ksa <p>"
    return HttpResponse(content)