from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.serializers import UserSerializer, UserRegisterSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class RetrieveUserView(generics.RetrieveAPIView):
    """View for retrieve user profile"""

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class ListUsersView(generics.ListAPIView):
    """View for retrieve users list"""
    serializer_class = UserSerializer

    def get_queryset(self) -> QuerySet:
        queryset = get_user_model().objects.all()

        email = self.request.query_params.get("email")

        if self.request.user.is_authenticated and email:
            queryset = queryset.filter(email__icontains=email)

        return queryset
