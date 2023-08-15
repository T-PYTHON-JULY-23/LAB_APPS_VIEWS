from django.shortcuts import render
from django.http import HttpRequest, HttpResponse 
# Create your views here.

def car_rentals_home(request:HttpRequest):
  content= "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
  return HttpResponse(content)

def car_info(request:HttpRequest):
  content= "Car rental agencies primarily serve people who require a temporary vehicle, for example, those who do not own their own car, travelers who are out of town, or owners of damaged or destroyed vehicles who are awaiting repair or insurance compensatione."
  return HttpResponse(content)
  