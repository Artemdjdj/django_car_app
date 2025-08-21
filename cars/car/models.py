from django.db import models
from django.contrib import admin


class CarBrand(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name="Название марки")
    slug = models.SlugField(max_length=120, unique=True, blank=True, null=True, verbose_name="Доменное имя")
    image = models.ImageField(upload_to="car_brand_images", verbose_name = "Изображение", blank=True, null=True)
    
    class Meta:
        db_table = "CarBrand"
        verbose_name_plural = "Бренды"
        verbose_name = "Бренд"
    def __str__(self):
        return self.name
    
class CarCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название",unique=True )
    slug = models.SlugField(max_length=50, verbose_name ="Доменное имя", unique=True)

    class Meta:
        db_table = "СarCategory"
        verbose_name_plural = "Категории автомобилей"
        verbose_name = "Категория автомобилей"
        
    def __str__(self):
        return self.name
    

    
class Car(models.Model):
    brand = models.ForeignKey(to='CarBrand', blank=True, null=True, on_delete=models.CASCADE, verbose_name="Марка")
    category = models.ForeignKey(to='CarCategory',blank=True, null=True, on_delete = models.CASCADE, verbose_name="Категория")
    model = models.CharField(max_length=100, verbose_name = "Модель")
    price = models.DecimalField(max_digits=15,decimal_places=3,verbose_name="Цена")
    mileage = models.DecimalField(max_digits=15,decimal_places=3, verbose_name="Пробег")
    year_produced  = models.IntegerField(verbose_name="Дата производства", null=True, blank=True)
    date_of_technical_maintenance = models.DateField(verbose_name= "Дата последнего ТО",null=True, blank=True)
    is_broken = models.BooleanField(default=False, verbose_name="Попадание в ДТП")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    country = models.CharField(blank=True, null=True, verbose_name="Страна производства")
    color= models.CharField(max_length=50,verbose_name = "Цвет")
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name="Доменное имя")
    
    class Meta:
        abstract=True
        
    def dollar_to_by(self):
        return self.price * 2.984
        



class FuelCar(Car):
    
    FUEL_TYPES = [
        ('gasoline', 'Бензин'),
        ('diesel', 'Дизель'),
        ('gas', 'Газ'),
    ]
    
    fuel_type = models.CharField(
        max_length=20, 
        choices=FUEL_TYPES,
        verbose_name="Тип топлива"
    )
    
    TRANSMISSION_TYPES = [
        ('mechanical', 'Механическая'),
        ('automatic', 'Автоматическая'),
        ('robotic', 'Робот'),
    ]
    
    transmission = models.CharField(
        max_length=20, 
        choices=TRANSMISSION_TYPES,
        default = TRANSMISSION_TYPES[0],
        verbose_name="Тип коробки передач"
    )
    
    engine_displacement = models.IntegerField(verbose_name="Объем двигателя", null=True, blank=True)
    fuel_consumption = models.FloatField(verbose_name="Расход топлива (л/100км)")
    fuel_tank_capacity = models.IntegerField(verbose_name="Объем топливного бака (л)")

    class Meta:
        verbose_name = "Автомобиль на топливе"
        verbose_name_plural = "Автомобили на топливе"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year_produced}) - {self.get_fuel_type_display()}"

    def get_main_picture(self):
        return self.images.filter(is_main=True).first().image



class ElectricCar(Car):
    battery_capacity = models.IntegerField(verbose_name="Емкость батареи (кВт⋅ч)")
    range = models.IntegerField(verbose_name="Запас хода (км)")
    charging_time = models.FloatField(verbose_name="Время полной зарядки (ч)")
    motor_power = models.IntegerField(verbose_name="Мощность двигателя (кВт)")

    class Meta:
        verbose_name = "Электромобиль"
        verbose_name_plural = "Электромобили"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year_produced}) - Электро"
    
    
class BaseCarImage(models.Model):
    image = models.ImageField(upload_to='cars/')
    is_main = models.BooleanField(default=False, verbose_name="Главное фото")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
        
class FuelCarImage(BaseCarImage):
    car = models.ForeignKey(
        FuelCar, 
        related_name='images', 
        on_delete=models.CASCADE,
        verbose_name="Автомобиль"
    )
    
    class Meta:
        verbose_name = "Фото автомобиля на топливе"
        verbose_name_plural = "Фото автомобилей на топливе"
        
    def str(self):
        return f"Фото {self.car.brand} {self.car.model}"

class ElectricCarImage(BaseCarImage):
    car = models.ForeignKey(
        ElectricCar, 
        related_name='images', 
        on_delete=models.CASCADE,
        verbose_name="Электромобиль"
    )
    
    class Meta:
        verbose_name = "Фото электромобиля"
        verbose_name_plural = "Фото электромобилей"
        
    def str(self):
        return f"Фото {self.car.brand} {self.car.model}"
    