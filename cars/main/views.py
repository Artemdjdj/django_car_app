from django.shortcuts import render
from django.http import HttpResponse
from car.models import Car

def index(request):
    cars = Car.objects.all()
    context ={
        'cars':cars,
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')
# Create your views here.
