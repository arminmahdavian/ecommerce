from django.urls import path
from .views import CartView, CartItemCreateView, CartItemDetailView


app_name = 'cart'
urlpatterns = [
    path('', CartView.as_view(), name='cart_list'),
    path('items/new/', CartItemCreateView.as_view(), name='cart_item_create'),
    path('items/<int:pk>/', CartItemDetailView.as_view(), name='cart_item_detail'),
]
