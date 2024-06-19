from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('product/<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('category/<slug:slug>/', views.ProductInCategory.as_view(), name='product_in_category'),
    path('favotites/', views.FavoriteList.as_view(), name='favorites'),
    path('add_favotite/<slug:slug>/', views.add_delete_favorite, name='in_favorite'),
    path('search/', views.search, name='search'),
]
