from django.contrib import admin
from .models import Order


# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'created_at', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'product__name')







