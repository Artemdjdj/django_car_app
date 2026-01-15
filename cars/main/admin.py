from django.contrib import admin
from main.models import UserWishes


class UserWishesAdmin(admin.ModelAdmin):
    list_display=['wish', 'user']
    search_fields=['user']
    
admin.site.register(UserWishes, UserWishesAdmin)