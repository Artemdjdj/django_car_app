from django.contrib import admin
from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('about/', views.about, name="about"),
    path('about/comment/<int:wish_id>/', views.wish, name="wish"),
    path('about/add_wish/', views.add_wish, name="add_wish"),
    path('', views.index, name="index") 
]
