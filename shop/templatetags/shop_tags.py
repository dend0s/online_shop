from django import template
from shop.models import Category, Favorite
from django.utils import timezone

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag(takes_context=True)
def get_count_favorite(context):
    request = context['request']
    if request.user.is_authenticated:
        return Favorite.objects.filter(user=request.user).count()


@register.filter(name='discount')
def discount(value):
    return int(value * 0.85)


@register.filter(name='new')
def new(date):
    now = timezone.now()
    date1 = now - date
    # if date1.days <= 7:
    return 'НОВИНКА' if date1.days <= 50 else ''
