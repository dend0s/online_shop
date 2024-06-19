from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.core.validators import MinValueValidator


class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True, max_length=250)
    description = models.TextField(verbose_name='Описание')
    characteristic = models.TextField(verbose_name='Характеристики')
    image = models.ImageField(upload_to='item_photo/', blank=True, verbose_name='Изображение')
    price = models.IntegerField(validators=[MinValueValidator(1)], verbose_name='Цена')
    quantity = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Количество')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    time_create = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='items', verbose_name='Категория')

    class Meta:
        ordering = ('-time_create',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=150, verbose_name='Описание')
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    @admin.display(description='Кол-во позиций')
    def get_count_positions(self):
        return Item.objects.filter(category=self).count()

    @admin.display(description='Кол-во товаров')
    def get_count_items(self):
        return sum([item.quantity for item in Item.objects.filter(category=self)])


class Favorite(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
