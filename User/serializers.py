from django.core.validators import RegexValidator
from rest_framework import serializers
from .models import *
from User.models import (
    User,
    Profile,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'phone_number'
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'province', 'city', 'address_detail', 'postal_code', 'receiver_name', 'customer', 'receiver_phone_number')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # customer = CustomerSerializer(read_only=True, many=True)
    address = serializers.HyperlinkedRelatedField(view_name='user_addresses', many=True, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
        extra_fields = ('address', 'information', 'wish_list', 'order_history')
