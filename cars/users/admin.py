from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display=['username', 'phone', 'email']
    list_filter = ['username', 'email']
    search_fields=['username', 'email']
    
admin.site.register(User, UserAdmin)