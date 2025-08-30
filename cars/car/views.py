from django.shortcuts import render
from .models import FuelCar, ElectricCar, CarBrand, CarCategory
# Create your views here.
def catalog(request, category_slug):
    if category_slug == "vse-kategorii":
        cars = FuelCar.objects.all()
    else:
        cars = FuelCar.objects.filter(category__slug = category_slug)
    categories = CarCategory.objects.all()
    print(categories)
    context ={
        'cars':cars,
        'categories':categories,
    }
    return render(request, 'main/index.html', context)

def car_info(request, car_slug):
    car = FuelCar.objects.get(slug = car_slug)
    brand = CarBrand.objects.get(name=car.brand)
    context = {
        'car':car,
        'brand':brand,
    }
    return render(request, 'car/car.html', context)