from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView

from .forms import QuantityForm
from .models import CartProducts
from shop.models import Item


class CartItemList(LoginRequiredMixin, ListView):
    context_object_name = 'items'
    template_name = 'cart.html'

    def get_queryset(self):
        return CartProducts.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        user = get_user_model().objects.get(username=self.request.user.username)
        if self.object_list:
            context['total_price'] = sum([item.get_total_price() for item in user.cart_products.all()])
            context['total_count'] = sum([item.quantity for item in user.cart_products.all()])
        return context


@login_required
def add_to_cart(request, slug):
    product = Item.objects.get(slug=slug, available=True)
    form = QuantityForm(request.POST)
    if form.is_valid():
        count = form.cleaned_data['quantity']
        update_basket = CartProducts.objects.filter(user=request.user, product=product).first()
        if update_basket:
            update_basket.quantity = (update_basket.quantity + count)
            update_basket.save()
        else:
            CartProducts.objects.create(user=request.user, product=product, quantity=count)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_from_cart(request, slug):
    product = Item.objects.get(slug=slug)
    CartProducts.objects.filter(user=request.user, product=product).delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def cart_clear(request):
    CartProducts.objects.filter(user=request.user).delete()
    return redirect('cart')
