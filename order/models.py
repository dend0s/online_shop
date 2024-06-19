from django.contrib.auth import get_user_model
from django.db import models
from shop.models import Item


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders',
                             verbose_name='Покупатель')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона')
    city = models.CharField(max_length=50, verbose_name='Город')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    pay_status = models.BooleanField(default=False, verbose_name='Оплачено')
    completed = models.BooleanField(default=False, verbose_name='Завершен')
    delivery = models.CharField(max_length=100, verbose_name='Доставка')
    pay_method = models.CharField(max_length=100, verbose_name='Способ оплаты')
    total_price = models.IntegerField(blank=True, null=True, verbose_name='Сумма к оплате')

    class Meta:
        ordering = ('date',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ: {self.pk}'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def get_total_price(self):
        return self.price * self.quantity
