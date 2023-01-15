from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderAllDetailSerializer, OrderViewSerializer


class OrderView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderViewSerializer

    def get_queryset(self):
        if self.action == ['list']:
            return Order.objects.filter(user=self.request.user)
        else:
            return super(OrderView, self).get_queryset()


class Send_Order