from django.shortcuts import render
from django.http import HttpResponse
from car.models import FuelCar, CarCategory
from main.models import UserWishes
from main.forms import WisheForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

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

def wish(request, wish_id):
    wish = UserWishes.objects.get(id=wish_id)
    context = {
        'wish':wish,
    }
    return render(request, 'main/comment.html', context)

@login_required
def add_wish(request):
    user_wish = UserWishes.objects.filter(user=request.user).first()
    # user_wish = UserWishes.objects.get(user=request.user)
    if request.method == "POST":
        if user_wish:
            form = WisheForm(data=request.POST, instance = user_wish)
        else:
            form = WisheForm(data=request.POST)
        if form.is_valid():
            wish = form.save(commit=False)
            wish.user = request.user
            wish.save()
            return HttpResponseRedirect(reverse('main:about'))
    else:
        if user_wish:
            form = WisheForm(instance = user_wish)
        else:
            form = WisheForm()
    
    context = {
        'form':form,
    }
    return render(request, 'main/add_wish.html', context)

