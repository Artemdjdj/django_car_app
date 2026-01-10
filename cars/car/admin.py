from django.contrib import admin

# Register your models here.
from .models import CarBrand, CarCategory, FuelCar, ElectricCar, FuelCarImage, ElectricCarImage

# admin.site.register(CarBrand)

class CarBrandAdmin(admin.ModelAdmin):
    prepopulated_fields  = {'slug':('name',)}
    list_display=['name', 'slug', 'image']
    search_fields=['name', 'slug']
    
class CarCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display=['name']
    search_fields=['name']
    
    
class CarImageInlineBase(admin.TabularInline):
    extra = 10

class FuelCarInline(CarImageInlineBase):
    model = FuelCarImage
    
class ElectricCarInline(CarImageInlineBase):
    model = ElectricCarImage
    
@admin.register(FuelCarImage)
class FuelCarImageAdmin(admin.ModelAdmin):
    list_display = ['car__brand','is_main']
    list_filter = ['car__brand','is_main']
    
@admin.register(ElectricCarImage)
class ElectricCarImageAdmin(admin.ModelAdmin):
    list_display = ['car__brand','is_main']
    list_filter = ['car__brand','is_main']

class FuelCarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('brand','model', 'mileage', 'price', 'color',)}
    list_display = ['brand', 'model', 'color', 'engine_displacement', 'price']
    list_filter = ['brand', 'color', 'price','is_broken']
    search_fields = ['brand', 'color', 'price']
    
class ElectricCarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('brand','model','mileage', 'price', 'color',)}
    list_display = ['brand', 'model', 'color', 'battery_capacity', 'price']
    list_filter = ['brand', 'color', 'price','is_broken']
    search_fields = ['brand', 'color', 'price']

    
admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(CarCategory,CarCategoryAdmin)
admin.site.register(FuelCar, FuelCarAdmin)
admin.site.register(ElectricCar, ElectricCarAdmin)