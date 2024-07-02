# from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrReadOnly
from .models import CustomUser
from .serializers import UserSerializer


# Create your views here.


class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# by APIView
class UserListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        # if request.user.is_staff:
        #     users = CustomUser.objects.all()
        # else:
        #     users = CustomUser.objects.filter(id=request.user.id)
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        self.check_object_permissions(self.request, user)
        return user

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







# # by Viewsets
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
#
#     def get_queryset(self):
#         if self.request.user.is_staff:
#             return CustomUser.objects.all()
#         return CustomUser.objects.filter(id=self.request.user.id)
#         # return CustomUser.objects.all()
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#     def perform_update(self, serializer):
#         serializer.save()










