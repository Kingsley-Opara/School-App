from django.shortcuts import render
from rest_framework.generics import (
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
)
from django.contrib.auth import get_user_model
from .serializers import UserSerializers
from rest_framework import permissions, authentication
from .permissions import UserPerm
from .authentication import TokenAuthentication
# Create your views here.

User = get_user_model()

class UserCreateListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, UserPerm]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class UserRetriveUpdateView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, UserPerm]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    def perform_update(self, serializer):
        return super().perform_update(serializer)

class UserDestoryView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, UserPerm]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]