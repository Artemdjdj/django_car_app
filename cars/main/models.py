from django.db import models
from django.conf import settings


class UserWishes(models.Model):
    wish = models.TextField(max_length=500,verbose_name="Отзыв")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        db_table = "wishes"
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        
        
