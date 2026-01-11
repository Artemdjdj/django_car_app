from django.contrib import admin
from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('about/', views.about, name="about"),
    path('', views.index, name="index") 
]
