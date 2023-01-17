from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order, OrderSend
from .serializers import OrderAllDetailSerializer, OrderViewSerializer, OrderSendSerializer, OrderSendCreateSerializer
from .utils import orders, order_items
from rest_framework.parsers import FormParser, JSONParser


class OrderView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderViewSerializer
    queryset = Order.objects.prefetch_related('order_items').all()

    def get_object(self):
        obj = super(OrderView, self).get_object()
        orders.check_order(obj)
        return obj

    def get_queryset(self):
        if self.action == 'list':
            return Order.objects.filter(user=self.request.user)
        else:
            return super(OrderView, self).get_queryset()


class CheckoutView(viewsets.ModelViewSet):
    queryset = OrderSend.objects.all()
    permission_classes = [IsAuthenticated]
    parser_classes = (FormParser, JSONParser)

    def get_queryset(self):
        return self.request.user.accounts.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderSendCreateSerializer
        else:
            return OrderSendSerializer
