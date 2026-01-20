from django.contrib import admin
from django.urls import path
from car import views

app_name = 'car'

urlpatterns = [
    path('car/add_new_car/', views.add_new_car, name="add_new_car"),
    path('car/add_new_car/add_car_image/<slug:type_of_car_slug>/<slug:car_slug>/', views.add_car_image, name="add_car_image"),
    path('<slug:category_slug>/', views.catalog, name="catalog"),
    path('car/<slug:car_slug>/', views.car_info, name="car_info"),
]
