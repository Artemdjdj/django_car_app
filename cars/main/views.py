from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Home")

def about(request):
    return HttpResponse("About")
# Create your views here.
