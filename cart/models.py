from django.contrib.auth import get_user_model
from django.db import models
from shop.models import Item


class CartProducts(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='cart_products')
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_total_price(self):
        return self.quantity * self.product.price

