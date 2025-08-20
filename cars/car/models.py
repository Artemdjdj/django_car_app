from django.db import models


class CarBrand(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name="Название марки")
    slug = models.SlugField(max_length=120, unique=True, blank=True, null=True, verbose_name="Доменное имя")
    
    class Meta:
        db_table = "CarBrand"
        verbose_name_plural = "Бренды"
        verbose_name = "Бренд"
    def __str__(self):
        return self.name

    
    
    
class Car(models.Model):
    
    brand = models.ForeignKey(to='CarBrand', on_delete=models.CASCADE, verbose_name="Марка")
    model = models.CharField(max_length=100, verbose_name = "Модель")
    price = models.DecimalField(max_digits=15,decimal_places=3,verbose_name="Цена")
    mileage = models.DecimalField(max_digits=15,decimal_places=3, verbose_name="Пробег")
    year_produced  = models.IntegerField(verbose_name="Дата производства", null=True, blank=True)
    date_of_technical_maintenance = models.DateField(verbose_name= "Дата последнего ТО",null=True, blank=True)
    is_broken = models.BooleanField(default=False, verbose_name="Попадание в ДТП")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    country = models.CharField(blank=True, null=True, verbose_name="Страна производства")
    image = models.ImageField(upload_to='car_images', blank=True, null=True, verbose_name="Изображение")
    
    
    class Meta:
        db_table = "Car"
        verbose_name_plural = "Автомобили"
        verbose_name = "Автомобиль"
    
    
    