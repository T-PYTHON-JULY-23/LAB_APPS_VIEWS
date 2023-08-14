from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Movie_Name(request):
    return HttpResponse("This page displays information about the movies")