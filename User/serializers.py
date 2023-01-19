from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'province', 'city', 'address_detail', 'postal_code', 'receiver_name', 'customer', 'receiver_phone_number')


class ProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
