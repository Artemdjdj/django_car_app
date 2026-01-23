from django import forms
from .models import CarBrand, FuelCar, ElectricCar, CarCategory, CarModel, FuelCarImage, ElectricCarImage
from multiupload.fields import MultiFileField     
        
class BaseCarForm(forms.ModelForm):
    images = MultiFileField(min_num=0, max_num=10, required=False, attrs={'class': 'form-control'})
    category = forms.CharField()
    model = forms.CharField()
    price = forms.IntegerField()
    mileage = forms.IntegerField()
    year_produced = forms.IntegerField()
    date_of_technical_maintenance = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    is_broken = forms.BooleanField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    country = forms.CharField(required=False)
    color = forms.CharField()

class FuelCarForm(BaseCarForm):
    fuel_type = forms.ChoiceField(
        choices=FuelCar.FUEL_TYPES,
        widget=forms.Select
    )
    transmission = forms.ChoiceField(
        choices=FuelCar.TRANSMISSION_TYPES,
        widget=forms.Select
    )
    engine_displacement = forms.IntegerField(required=False)
    fuel_consumption = forms.FloatField()
    fuel_tank_capacity = forms.IntegerField()
    class Meta:
        model = FuelCar
        fields = [
            'price',
            'mileage',
            'year_produced',
            'date_of_technical_maintenance',
            'is_broken',
            'description',
            'country',
            'color',
            'fuel_type',
            'transmission',
            'engine_displacement',
            'fuel_consumption',
            'fuel_tank_capacity',
            
        ]
        
        widgets = {
            'date_of_technical_maintenance': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        
class ElectricCarForm(BaseCarForm):
    battery_capacity = forms.CharField()
    range = forms.CharField()
    charging_time = forms.CharField()
    motor_power = forms.CharField()
    class Meta:
        model = FuelCar
        model = ElectricCar
        fields = [
            'price',
            'mileage',
            'year_produced',
            'date_of_technical_maintenance',
            'is_broken',
            'description',
            'country',
            'color',
            'battery_capacity',
            'range',
            'charging_time',
            'motor_power'
        ]
        
        widgets = {
            'date_of_technical_maintenance': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }