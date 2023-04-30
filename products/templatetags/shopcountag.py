from django import template

from products.models import Basket
from products.models import ProductCategory

register = template.Library()


@register.simple_tag
def categorylist():
    return ProductCategory.objects.all()


@register.simple_tag
def shopcartcount(userid):
    count = Basket.objects.filter(user_id=userid).count()
    return count