from django import template
from car.models import CarCategory
from django.utils.http import urlencode

register = template.Library()


@register.simple_tag
def get_url():
    category = CarCategory.objects.get(slug = "vse-kategorii")
    return  category.slug


# Для того чтобы после применения фильтров не слетала пагинация
@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
# urlencode из словаря делает адрес