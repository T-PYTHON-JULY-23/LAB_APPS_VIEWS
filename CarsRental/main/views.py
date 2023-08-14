from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def home(request: HttpRequest):
    content= "Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    return HttpResponse(content)

def info(request: HttpRequest):
    content="Car rentals provide convenient access to vehicles for a specific period of time. "
    return HttpResponse(content)

