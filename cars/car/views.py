from django.shortcuts import render
from .models import FuelCar, ElectricCar, CarBrand, CarCategory
from django.core.paginator import Paginator
from .utils import get_all_cars

from .models import FuelCar, ElectricCar
from itertools import chain

def catalog(request, category_slug):
    page_number = request.GET.get("page")
    order_by = request.GET.get("order_by", None)
    
    #params to find special cars
    brand = request.GET.get("brand", None)
    model = request.GET.get("model", None)
    max_mileage = request.GET.get("max_mileage", None)
    # type_of_transmission = request.GET.get("type_of_transmission", None)
    year_before = request.GET.get("year_before", None)
    year_after = request.GET.get("year_after", None)
    # type_of_oil = request.GET.get("type_of_oil", None)
    max_price = request.GET.get("max_price", None)
    
    
    #getting special cars
    fuel_cars = FuelCar.objects.all();
    if brand:
        fuel_cars = fuel_cars.filter(brand__name__iexact = brand)
    if model:
        fuel_cars = fuel_cars.filter(model__iexact = model)
    if max_mileage:
        fuel_cars = fuel_cars.filter(mileage__lte = max_mileage)
    if max_price:
        fuel_cars = fuel_cars.filter(price__lte = max_price)
    if year_before:
        fuel_cars = fuel_cars.filter(year_produced__gte= year_before)
    if year_after:
        fuel_cars = fuel_cars.filter(year_produced__lte= year_after)
    
    electric_cars = ElectricCar.objects.all()
    
    if brand:
        electric_cars = electric_cars.filter(brand__name__iexact = brand)
    if model:
        electric_cars = electric_cars.filter(model__iexact = model)
    if max_mileage:
        electric_cars = electric_cars.filter(mileage__lte = max_mileage)
    if max_price:
        electric_cars = electric_cars.filter(price__lte = max_price)
    if year_before:
        electric_cars = electric_cars.filter(year_produced__gte= year_before)
    if year_after:
        electric_cars = electric_cars.filter(year_produced__lte= year_after)
        
    cars = list(chain(fuel_cars, electric_cars))
    # cars = list(chain(
    #     FuelCar.objects.filter(brand__name__iexact = brand, model__iexact = model, mileage__lte=max_mileage, price),
    #     ElectricCar.objects.all()
    # ))
    #filters
    # if order_by and order_by!= "default":
    #     cars = cars.order_by(order_by)
    
    
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