from django.shortcuts import render
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from car.models import FuelCar, ElectricCar
from django.contrib.auth.decorators import login_required

def login(request):
    
    if request.method == "POST":
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
        
    context = {
        'form':form,
    }
    return render(request,"users/login.html", context)


def registration(request):
    BACKEND = 'django.contrib.auth.backends.ModelBackend'
    if request.method == "POST":
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user, backend=BACKEND)
            return HttpResponseRedirect(reverse('main:index'))
            # return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()
        
    context = {
        'form':form,
    }
    
    return render(request,"users/registration.html", context)

@login_required
def profile(request):
    current_user = request.user
    fuel_cars = FuelCar.objects.filter(user = current_user)
    electric_cars = ElectricCar.objects.filter(user = current_user)
    
    context = {
        'fuel_cars':fuel_cars,
        'electric_cars':electric_cars
    }
    return render(request,"users/profile.html", context)

@login_required
def profile_settings(request):
    if request.method == "POST":
        form = ProfileForm(data = request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance = request.user)
        
    context = {
        'form':form,
    }
    return render(request, "users/profile_settings.html", context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))
