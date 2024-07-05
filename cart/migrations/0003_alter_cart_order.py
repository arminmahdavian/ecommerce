# Generated by Django 5.0.6 on 2024-07-03 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_order'),
        ('orders', '0003_remove_order_cart_order_product_order_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_order', to='orders.order'),
        ),
    ]