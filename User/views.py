from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


class UserAddress(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.filter(is_valid=True)
