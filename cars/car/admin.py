from django.contrib import admin

# Register your models here.
from .models import CarBrand,  Car

# admin.site.register(CarBrand)

class CarBrandAdmin(admin.ModelAdmin):
    prepopulated_fields  = {'slug':('name',)}
    list_display=['name', 'slug']
    search_fields=['name', 'slug']

class CarAdmin(admin.ModelAdmin):
    
    list_display=['brand__name', 'model', 'mileage','price', 'year_produced']
    search_fields=['brand__name','model', 'price']
    
admin.site.register(Car, CarAdmin)

    
admin.site.register(CarBrand, CarBrandAdmin)