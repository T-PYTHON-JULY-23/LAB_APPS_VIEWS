from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def view_welcome(requset:HttpRequest):
    content="Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    return HttpResponse(content)

def carsrental(requset:HttpRequest):
    con="Car rental services provide a convenient and flexible solution for individuals and businesses in need of temporary transportation."
    return HttpResponse(con)
