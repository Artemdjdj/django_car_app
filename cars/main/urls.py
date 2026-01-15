from django.contrib import admin
from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('about/', views.about, name="about"),
    path('about/comment/<int:wishe_id>/', views.comment, name="wishe"),
    path('', views.index, name="index") 
]
