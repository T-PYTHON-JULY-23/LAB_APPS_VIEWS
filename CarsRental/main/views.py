from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request: HttpRequest):
    content = "Hello World, This is my new HOME for Car Rentals Website! we're excited to welcome you here."
    return HttpResponse(content)


def info_view(request: HttpRequest):

    content = "<h2 style='color:green;'> A simple paragraph about Car Rentals. </h2>"

    return HttpResponse(content)
