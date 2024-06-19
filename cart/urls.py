from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartItemList.as_view(), name='cart'),
    path('add/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('delete/<slug:slug>/', views.delete_from_cart, name='delete_from_cart'),
    path('clear/', views.cart_clear, name='cart_clear'),
]
