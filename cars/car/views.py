from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import FuelCar, ElectricCar, CarBrand, CarCategory, CarModel
from django.core.paginator import Paginator
from .utils import filter_fuel_car, filter_electric_car, get_all_cars
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.db.models import Q
from .forms import FuelCarForm, ElectricCarForm, FuelCarImageForm, ElectricCarImageForm

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
    
    
    
@login_required
def add_new_car(request):
    models = None
    selected_brand = None
    selected_model = None
    selected_brand_name = None
    form=None
    categories = CarCategory.objects.exclude(slug='vse-kategorii')
    if request.method == "POST":
        type_of_form = request.POST.get('type_of_form')
        selected_model= request.POST.get('model')
        if type_of_form and type_of_form == 'electro_car':  
            brands = CarBrand.objects.filter(Q(is_fuel_brand=False) | Q(is_fuel_brand__isnull=True))
        else:
            brands = CarBrand.objects.filter(Q(is_fuel_brand=True) | Q(is_fuel_brand__isnull=True))
        action = request.POST.get('action')
        if action == 'create_car':
            form = FuelCarForm(data=request.POST) if type_of_form=="fuel_car" else ElectricCarForm(data=request.POST)
            brand_id = request.POST.get('brand')
            model_name = request.POST.get('model')
            category_id = request.POST.get('category')

            if form.is_valid():
                new_form = form.save(commit=False)
                brand = CarBrand.objects.get(id=int(brand_id))
                model = CarModel.objects.get(name__iexact=model_name)
                category = CarCategory.objects.get(id=int(category_id))

                new_form.brand = brand
                new_form.category = category
                new_form.model = model
                new_form.user = request.user
                new_form.save()

                car_slug = new_form.slug
                return HttpResponseRedirect(reverse('car:add_car_image', kwargs={
                    'type_of_car_slug':type_of_form,
                    'car_slug': car_slug,
                }))
        else:
            selected_brand = request.POST.get('brand')
            type_of_form = request.POST.get('type_of_form')
            if selected_brand:
                my_brand = CarBrand.objects.get(id = selected_brand)
                selected_brand_name =my_brand.name
                models = CarModel.objects.filter(brand = my_brand.id) if selected_brand else None
                if type_of_form and type_of_form=='fuel_car':
                    form = FuelCarForm(data=request.POST)
                    models = models.filter(is_fuel_model = True)
                else:
                    form = ElectricCarForm(data=request.POST)
                    models = models.filter(is_fuel_model = False)
    else:
        type_of_form = request.GET.get('type_of_form')
        if type_of_form and type_of_form == 'electro_car':  
            form = ElectricCarForm()
            brands = CarBrand.objects.filter(Q(is_fuel_brand=False) | Q(is_fuel_brand__isnull=True))
        else:
            form = FuelCarForm()
            brands = CarBrand.objects.filter(Q(is_fuel_brand=True) | Q(is_fuel_brand__isnull=True))
    
    context = {
        'form':form,
        'brands': brands,
        'models': models,
        'categories':categories,
        'selected_brand':selected_brand,
        'selected_brand_name':selected_brand_name,
        'selected_model':selected_model,
        'type_of_form':type_of_form,
    }
    
    return render(request, 'car/add_new_car.html', context)


@login_required
def add_car_image(request, type_of_car_slug, car_slug):
    form = None
    if request.method == "POST":
        form = FuelCarImageForm(request.POST, request.FILES) if type_of_car_slug == 'fuel_car' else ElectricCarImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            car = FuelCar.objects.get(slug=car_slug) if type_of_car_slug=='fuel_car' else ElectricCar.objects.get(slug=car_slug)
            new_form.car = car
            new_form.save()

            if request.POST.get('action')=="save_and_next":
                return HttpResponseRedirect(reverse('car:add_car_image', kwargs={
                    'type_of_car_slug': type_of_car_slug,
                    'car_slug': car_slug,
                }))
            else:
                return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = FuelCarImageForm()  if type_of_car_slug == 'fuel_car' else ElectricCarImageForm()
    
    context = {
        'form':form,
        'type_of_car_slug':type_of_car_slug,
        'car_slug':car_slug,
    }
    
    return render(request, 'car/add_image_to_car.html', context)