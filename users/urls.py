from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import UserViewSet
from .views import UserListView, UserDetailView, UserCreateView

app_name = 'users'

# router = DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('users/', UserListView.as_view(), name="user_list"),
    path('users/register/', UserCreateView.as_view(), name="create_user"),
    path('users/<int:pk>/', UserDetailView.as_view(), name="user_detail"),

]