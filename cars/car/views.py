from django.shortcuts import render
from .models import FuelCar, ElectricCar, CarBrand
# Create your views here.
def catalog(request):
    pass

def car_info(request, car_slug):
    car = FuelCar.objects.get(slug = car_slug)
    brand = CarBrand.objects.get(name=car.brand)
    context = {
        'car':car,
        'brand':brand,
    }
    return render(request, 'car/car.html', context)