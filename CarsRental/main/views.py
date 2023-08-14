from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def helo_view(request: HttpRequest) -> HttpResponse:
    content = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(content)

def car_rental_page(request: HttpRequest) -> HttpResponse:
    content = "<body><h1>the cars we have is in great quality, and with a good price</h1><h4>Hyundai accent 2016 / 120 SR in a day</h4><h4>Toyota corolla 2020 / 220 SR in a day</h4></body>"
    return HttpResponse(content)

# Create your views here.
