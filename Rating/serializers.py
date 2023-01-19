from rest_framework import serializers

from Rating import models


class RatedSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.RatedItem
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    rated_object = RatedSerializer
    class Meta:
        model  = models.Rating
        fields = '__all__'