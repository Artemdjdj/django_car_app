from django.shortcuts import render
from .models import FuelCar, ElectricCar, CarBrand, CarCategory
from django.core.paginator import Paginator
from .utils import filter_fuel_car, filter_electric_car, get_all_cars

from .models import FuelCar, ElectricCar
from itertools import chain

def catalog(request, category_slug):
    page_number = request.GET.get("page")
    order_by = request.GET.get("order_by", None)
    search_type = request.GET.get("search_type", None)
    
    cars = None
    
    if not search_type or search_type == "fuel_car":
        cars = filter_fuel_car(request)
    else:
        cars = filter_electric_car(request)
    
        
        
    #filters
    if order_by and order_by!= "default":
        cars = cars.order_by(order_by)
    
    #pagination
    paginator = Paginator(cars,3)
    page_obj = paginator.get_page(page_number)
    
    categories = CarCategory.objects.all()
    
    context ={
        'categories':categories,
        'page_obj':page_obj,
        'category_slug': category_slug,
    }
    
    return render(request, 'car/catalog.html', context)

def car_info(request, car_slug):
    try:
        car = FuelCar.objects.get(slug = car_slug)
    except FuelCar.DoesNotExist:
        try:
            car = ElectricCar.objects.get(slug = car_slug)
        except ElectricCar.DoesNotExist:
            car = None
    if car:
        brand = CarBrand.objects.get(name=car.brand)
        context = {
            'car':car,
            'brand':brand,
        }
        return render(request, 'car/car.html', context)