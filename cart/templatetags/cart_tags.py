from django import template
from django.contrib.auth import get_user_model

from cart.models import CartProducts

register = template.Library()


@register.simple_tag(takes_context=True)
def user_cart(context):
    request = context['request']
    if request.user.is_authenticated:
        # user = get_user_model().objects.get(username=request.user.username)
        return {'total_price': sum([item.get_total_price() for item in request.user.cart_products.all()]),
                'total_count': sum([item.quantity for item in request.user.cart_products.all()]),
                'items': CartProducts.objects.filter(user=request.user)}
