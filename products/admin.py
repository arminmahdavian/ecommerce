from django.contrib import admin
from .models import Category, Product, ProductImage


# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'price', 'category', 'is_available', 'quantity', 'created_at', 'updated_at')
    list_filter = ('is_available', 'created_at', 'updated_at', 'category')
    list_editable = ('price', 'quantity', 'is_available')
    search_fields = ('name', 'description')
    # prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)



