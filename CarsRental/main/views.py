from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home(request: HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    return HttpResponse(content)


def info(request: HttpRequest):

    content = "Enjoy a Car Rental with unlimited kilometres & fees incl. In Business since 1912. More than 100 Years of Experience. Rent with SIXT and enjoy your ride! Book now & save! Customer service award. Over 180.000 vehicles. Free Cancellation Policy. Car Rental since 1912."

    return HttpResponse(content)