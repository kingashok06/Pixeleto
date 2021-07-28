from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView , ListAPIView
from .models import User
from .serializers import UserSerializers
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination


class UserList(ListCreateAPIView):
    serializer_class = UserSerializers
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return User.objects.filter(owner=self.request.user)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializers
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return User.objects.filter(owner=self.request.user)

class APIListview(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = PageNumberPagination
