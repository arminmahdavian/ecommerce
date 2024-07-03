from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import CategoryViewset, ProductViewset, NewProductViewset
from . import views


app_name = 'products'

# router = DefaultRouter()
# router.register(r'categories', CategoryViewset)
# router.register(r'products', ProductViewset)

urlpatterns = [
    # path('products/', include(router.urls)),
    path('products/', views.ProductListCreateView.as_view(), name='products_list_create'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='products_detail_detail'),
    path('categories/', views.CategoryListCreateView.as_view(), name='categories_list_create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='categories_detail'),

]