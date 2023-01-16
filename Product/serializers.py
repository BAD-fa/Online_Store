from rest_framework import serializers
from .models import Category, Product


# Category Related Serializers------------------------------------------------------------------------------------------
class ParentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class CategorySerializer(serializers.ModelSerializer):
    parent_category = ParentCategorySerializer(many=False, required=False, allow_null=True)

    class Meta:
        model = Category
        fields = ['title', 'parent_category']


# Product Related Serializers-------------------------------------------------------------------------------------------
class ProductSerializer(serializers.ModelSerializer):
    category = ParentCategorySerializer(many=False, required=False, allow_null=True)

    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'avatar', 'description', 'stock']
        extra_kwargs = {
            'avatar': {'required': False, 'allow_null': True},
        }
