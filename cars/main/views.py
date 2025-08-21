from django.shortcuts import render
from django.http import HttpResponse
from car.models import FuelCar

def index(request):
    cars = FuelCar.objects.all()
    context ={
        'cars':cars,
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')
# Create your views here.
