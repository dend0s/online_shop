from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Item, Favorite


def index(request):
    new_items = Item.objects.filter(available=True).order_by('-time_create')[:6]
    smartphones = Item.objects.filter(available=True, category__slug='smartphones')[:8]
    watches = Item.objects.filter(available=True, category__slug='watches')[:6]
    pods = Item.objects.filter(available=True, category__slug='pods')[:6]
    context = {
        'new_items': new_items,
        'smartphones': smartphones,
        'watches': watches,
        'pods': pods
    }
    return render(request, 'index.html', context)


class ProductList(ListView):
    context_object_name = 'products'
    template_name = 'product_list.html'
    paginate_by = 8

    def get_queryset(self):
        sort = self.request.GET.get('sort')
        if sort == 'price':
            return Item.objects.filter(available=True).order_by('price')
        elif sort == '-price':
            return Item.objects.filter(available=True).order_by('-price')
        return Item.objects.filter(available=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Все товары'
        return context


class ProductDetail(DetailView):
    model = Item
    context_object_name = 'product'
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['related_products'] = Item.objects.filter(available=True, category=self.object.category).exclude(
            slug=self.object.slug)[:4]
        if self.request.user.is_authenticated:
            context['favorite'] = Favorite.objects.filter(user=self.request.user, product=self.object)
        return context


class ProductInCategory(ListView):
    context_object_name = 'products'
    template_name = 'product_list.html'
    paginate_by = 8

    def get_queryset(self):
        return Item.objects.filter(available=True, category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = f'{self.object_list[0].category} {self.object_list[0].category.description}'
        return context


class FavoriteList(LoginRequiredMixin, ListView):
    template_name = 'favorite_list.html'
    context_object_name = 'favorites'

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


@login_required
def add_delete_favorite(request, slug):
    product = Item.objects.get(slug=slug)
    if item := Favorite.objects.filter(user=request.user, product=product):
        item.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    Favorite.objects.create(user=request.user, product=product)
    return redirect(request.META.get('HTTP_REFERER'))


def search(request):
    items = request.GET['q']
    products = Item.objects.filter((Q(name__icontains=items) | Q(slug__icontains=items)) & Q(available=True))
    context = {'products': products, 'title': 'Результаты поиска'}
    return render(request, 'product_list.html', context)
