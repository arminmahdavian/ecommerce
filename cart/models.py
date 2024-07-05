from django.db import models
from django.conf import settings
from products.models import Product
from orders.models import Order


# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, related_name='cart', blank=True, null=True)

    def __str__(self):
        return f"Cart for user {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} in cart for user {self.cart.user.username}'s cart"










