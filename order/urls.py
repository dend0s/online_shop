from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('active/', views.order_active_list, name='orders_active'),
    path('completed/', views.order_completed_list, name='orders_completed'),
    path('cancel/<int:pk>/', views.cancel_order, name='cancel_order')
]
