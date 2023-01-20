from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

BASE_DIR = 'http://127.0.0.1:8000/profile/'


class ProfileUrl(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get(self, request, *args, **kwargs):
        # profile = TODO show user profile that user login
        context = {
            'Address': BASE_DIR + 'address',
            'Information': BASE_DIR + 'information/<int:pk>',
            'wishlist': None,
            'history': None,
        }
        return Response(context, status.HTTP_200_OK)


class UserAddress(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.filter(is_valid=True)


class CustomerInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

# class OrderHistory(generics.ListAPIView):
#
