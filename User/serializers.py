from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'province', 'city', 'address_detail', 'postal_code', 'receiver_name', 'customer', 'receiver_phone_number')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = ('customer',)
