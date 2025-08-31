from django.shortcuts import render
from .models import FuelCar, ElectricCar, CarBrand, CarCategory
from django.core.paginator import Paginator

def catalog(request, category_slug):
    page_number = request.GET.get("page")
    order_by = request.GET.get("order_by", None)
    
    if category_slug == "vse-kategorii":
        cars = FuelCar.objects.all()
    else:
        cars = FuelCar.objects.filter(category__slug = category_slug)
    
    if order_by and order_by!= "default":
        cars = cars.order_by(order_by)
        
    paginator = Paginator(cars,1)
    page_obj = paginator.get_page(page_number)
    
    categories = CarCategory.objects.all()
    
    context ={
        'categories':categories,
        'page_obj':page_obj,
        'category_slug': category_slug,
    }
    return render(request, 'car/catalog.html', context)

def car_info(request, car_slug):
    car = FuelCar.objects.get(slug = car_slug)
    brand = CarBrand.objects.get(name=car.brand)
    context = {
        'car':car,
        'brand':brand,
    }
    return render(request, 'car/car.html', context)