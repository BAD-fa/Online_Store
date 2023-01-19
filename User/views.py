from django.shortcuts import render
from rest_framework import generics
from serializers import *


class UserAddress(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    queryset = AddressSerializer.objects.filter(is_valid=True)
