from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def welcome(request:HttpRequest):
    content="<h1 style='color:blue';>Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.</h1>"
    return HttpResponse(content)

def about(request:HttpRequest):
    content="<p style='color:green';>Car rental is a service provided by companies that allows individuals to temporarily use a vehicle in exchange for a fee.</p> "
    return HttpResponse(content)
