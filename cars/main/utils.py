from car.models import FuelCar, CarBrand

def get_brands(request):
    return CarBrand.objects.all()