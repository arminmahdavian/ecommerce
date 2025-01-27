from django.db import models
from django.conf import settings
from products.models import Product


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'pending'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled'),
    ], default='pending')

    def __str__(self):
        return f'Order {self.id}, {self.product.name}, by {self.product.user.username}'












