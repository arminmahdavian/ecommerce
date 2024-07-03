from django.urls import path, include
from .views import OrderListCreateView, OrderDetailView


app_name = 'orders'

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='orders_list_create'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order_detail'),

]



