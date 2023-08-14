from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def home(request:HttpRequest):
    content1 ="Hello World, This is my new HOME for Car Rentals Website ! we're excited to welcome you here."
    return HttpResponse(content1)

def about(request:HttpRequest):
    content2= " <h2 style='color:green;'> agency is a company that rents automobiles for short periods of time to the public.generally ranging from a few hours to a few weeks.<h2>"
    return HttpResponse(content2)
