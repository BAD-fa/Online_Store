from rest_framework import decorators
from rest_framework import viewsets

from Rating import models
from Rating import serializers


class RatingViewSet(viewsets.ModelViewSet):
    serializer_class  = serializers.RatingSerializer
    queryset          = models.Rating.objects.all()
    http_method_names = ['get', 'post']