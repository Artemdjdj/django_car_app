from django.shortcuts import render
from django.http import HttpResponse
from car.models import FuelCar, CarCategory


def index(request):
    cars = FuelCar.objects.all()
    categories = CarCategory.objects.all()
    print(categories)
    context ={
        'cars':cars,
        'categories':categories,
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

