from rest_framework import serializers
from .models import Category


# Category Related Serializers------------------------------------------------------------------------------------------
class ParentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class CategorySerializer(serializers.ModelSerializer):
    parent_category = ParentCategorySerializer(required=False, allow_null=True)

    class Meta:
        model = Category
        fields = ['title', 'parent_category']
