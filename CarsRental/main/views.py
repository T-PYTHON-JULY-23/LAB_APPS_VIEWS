from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def first_page(request : HttpRequest):
    content= "<h1>Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here.</h1>"
    return HttpResponse(content)

def info_page(request : HttpRequest):
    content = "<p>Certainly! A car rental website serves as an online platform where individuals can effortlessly browse, compare, and book rental vehicles for their travel needs.</p>"
    return HttpResponse(content)