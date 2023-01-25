from rest_framework.serializers import ModelSerializer
from models import WishList


class WishListSerializer(ModelSerializer):
    class Meta:
        model = WishList
        fields = ['id', 'name', 'user', 'product', 'created_time']
