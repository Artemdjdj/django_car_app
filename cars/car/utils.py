
from .models import FuelCar, ElectricCar
from itertools import chain

def get_all_cars():
    cars = list(chain(FuelCar.objects.all(),ElectricCar.objects.all()))
    return cars

def filter_fuel_car(request, ):
    brand = request.GET.get("brand", None)
    model = request.GET.get("model", None)
    max_mileage = request.GET.get("max_mileage", None)
    type_of_transmission = request.GET.get("type_of_transmission", None)
    year_before = request.GET.get("year_before", None)
    year_after = request.GET.get("year_after", None)
    type_of_oil = request.GET.get("type_of_oil", None)
    max_price = request.GET.get("max_price", None)
    
    print(type_of_transmission, type_of_oil)
    fuel_cars = FuelCar.objects.all()
    if brand:
        fuel_cars = fuel_cars.filter(brand__name__iexact = brand)
    if model:
        fuel_cars = fuel_cars.filter(model__iexact = model)
    if max_mileage:
        fuel_cars = fuel_cars.filter(mileage__lte = max_mileage)    
    if type_of_transmission and type_of_transmission != "default":
        fuel_cars = fuel_cars.filter(transmission__iexact = type_of_transmission)
    if type_of_oil and type_of_oil != "default":
        fuel_cars = fuel_cars.filter(fuel_type__iexact = type_of_oil)
    if max_price:
        fuel_cars = fuel_cars.filter(price__lte = max_price)
    if year_before:
        fuel_cars = fuel_cars.filter(year_produced__gte= year_before)
    if year_after:
        fuel_cars = fuel_cars.filter(year_produced__lte= year_after)
    return fuel_cars

def filter_electric_car(request):
    brand = request.GET.get("brand", None)
    model = request.GET.get("model", None)
    max_mileage = request.GET.get("max_mileage", None)
    year_before = request.GET.get("year_before", None)
    year_after = request.GET.get("year_after", None)
    max_price = request.GET.get("max_price", None)
    
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
        
    return electric_cars