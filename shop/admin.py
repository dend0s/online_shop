from django.contrib import admin
from .models import Item, Category


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'price', 'quantity', 'available', 'description', 'characteristic', 'image', 'category']
    list_display = ['name', 'price', 'quantity', 'category', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'get_count_positions', 'get_count_items']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')

