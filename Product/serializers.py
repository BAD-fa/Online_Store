from rest_framework import serializers

from Product.models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ("user", "product", "status", "total_price", "discount")


class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer()

    class Meta:
        model = CartItem
        fields = ("cart", "product", "expire_time", "count",)
