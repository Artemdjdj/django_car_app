from django.shortcuts import render
from .models import FuelCar, ElectricCar, CarBrand, CarCategory, CarModel
from django.core.paginator import Paginator
from .utils import filter_fuel_car, filter_electric_car, get_all_cars

from .models import FuelCar, ElectricCar
from itertools import chain
from django.db.models import Q

def catalog(request, category_slug):
    page_number = request.GET.get("page")
    # order_by = request.GET.get("order_by", None)
    search_type = request.GET.get("search_type", None)
    selected_brand = request.GET.get("brand", None)
    
    cars = None
    brands = None
    if not search_type or search_type == "fuel_car":
        cars = filter_fuel_car(request)
        brands = CarBrand.objects.filter(Q(is_fuel_brand=True) | Q(is_fuel_brand__isnull=True))
    else:
        cars = filter_electric_car(request)
        brands = CarBrand.objects.filter(Q(is_fuel_brand=False) | Q(is_fuel_brand__isnull=True))
    
    # brands = CarBrand.objects.all()
    
    models = None
    if selected_brand  and selected_brand!="default":
        my_brand = CarBrand.objects.get(name = selected_brand)
        models = CarModel.objects.filter(brand = my_brand.id) if selected_brand else None
        if search_type == "fuel_car":
            models = models.filter(is_fuel_model = True)
        elif search_type == "electro_car":
            models = models.filter(is_fuel_model = False)
            
    
    #orders
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
        'brands':brands,
        'models':models,
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