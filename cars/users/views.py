from django.shortcuts import render
from .forms import UserLoginForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

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
        form = UserLoginForm
    context = {
        'form':form,
    }
    return render(request,"users/login.html", context)


def registration(request):
    context = {
        
    }
    return render(request,"users/registration.html", context)


def profile(request):
    context = {
        
    }
    return render(request,"users/profile.html", context)


def logout(request):
    context = {
        
    }
    return render(request,"", context)
