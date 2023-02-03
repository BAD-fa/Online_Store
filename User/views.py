from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

BASE_DIR = 'http://127.0.0.1:8000/profile/'


class ProfileUrl(generics.RetrieveAPIView):
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get(self, request, *args, **kwargs):
        context = {
            'Address': BASE_DIR + 'address',
            'Information': BASE_DIR + 'information/<int:pk>',
            'wishlist': None,
            'history': None,
        }
        return Response(context, status.HTTP_200_OK)


class UserAddress(generics.ListCreateAPIView):
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializer
    queryset = Address.objects.filter(is_valid=True)


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]

        elif self.action == ['list', 'destroy']:
            return [IsAdminUser()]

        elif self.action == 'update':
            return [IsAuthenticated()]


class CustomerInfo(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = [IsAuthenticated]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

# class OrderHistory(generics.ListAPIView):
#
