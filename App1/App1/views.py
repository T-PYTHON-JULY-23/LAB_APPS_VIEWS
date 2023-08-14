from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request: HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    return HttpResponse(content)


def info_view(request: HttpRequest):

    content = "A car rental, hire car or car hire agency is a company that rents automobiles for short periods of time to the public, generally ranging from a few hours to a few weeks."

    return HttpResponse(content)