from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class UserAddress(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.filter(is_valid=True)


class CustomerInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    # queryset = Profile.objects.filter(customer__id=request.user.id)

    # def get(self, request, pk):
    #     customer = get_object_or_404(Customer, pk=pk)
    #     context = {
    #         'first name': customer.first_name,
    #         'last_name': customer.last_name,
    #         'username': customer.username,
    #         'email': customer.email,
    #         'birthday': customer.birthday,
    #         'national_id': customer.national_id,
    #         'phone_number': customer.phone_number
    #     }
    #     return Response(context, status=status.HTTP_200_OK)

