from django.contrib import admin
from django.urls import path
from car import views

app_name = 'car'

urlpatterns = [
    path('', views.catalog, name="catalog"),
    path('car/<slug:car_slug>/', views.car_info, name="car_info")
]
