from django.shortcuts import render
from django.http import HttpResponse
from car.models import FuelCar, CarCategory
from main.models import UserWishes

from django.core.paginator import Paginator
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
    wishes = UserWishes.objects.all();
    page_number = request.GET.get("page")
    
    #pagination
    paginator = Paginator(wishes,3)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj,
    }
    return render(request, 'main/about.html', context)

def comment(request, wishe_id):
    wishe = UserWishes.objects.get(id=wishe_id)
    context = {
        'wishe':wishe,
    }
    return render(request, 'main/comment.html', context)



