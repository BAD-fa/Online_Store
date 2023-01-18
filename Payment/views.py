from django.http import HttpRequest
from rest_framework.decorators import action
from rest_framework import viewsets, status, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Order, OrderSend, Gateway, Payment
from .serializers import (OrderViewSerializer, OrderSendCreateSerializer, GatewaySerialzier, PaymentSerializer)
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


class CheckoutView(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = OrderSend.objects.all().select_related('order')
    permission_classes = [IsAuthenticated]
    parser_classes = (FormParser, JSONParser)
    serializer_class = OrderSendCreateSerializer

    def get_object(self):
        obj = super(CheckoutView, self).get_object()
        if obj.order.status < 2:
            obj.order = orders.check_order(obj.order)
        return obj


class Payment(viewsets.ViewSet):

    @action(methods='get', detail=True, url_name='payments/order/<int:pk>/gateway/')
    def connect_to_gateway(self, request, pk=None):
        try:
            order = Order.objects.prefetch_related('order_items').get(pk=pk).select_related('order_send')
        except Order.DoesNotExist:
            return Response({"detail": 'order does not exist'}, status.HTTP_400_BAD_REQUEST)
        order = orders.check_order(order)
        order.order_items.filter(is_valid=False).delete()
        order_send = order.order_send
        total_price = order.orders_price + order_send.send_cost
        try:
            connection = Gateway.objects.get(user=request.user, order_id=str(order.id), amount=total_price)
        except Gateway.DoesNotExist:
            Gateway.objects.filter(order_id=str(order.id)).delete()
            connection = Gateway.objects.create(user=request.user, order_id=str(order.id),
                                                amount=total_price,
                                                callbacl=f'domain/payments/order/{pk}/gateway/')
        serializer = GatewaySerialzier(instance=connection)
        response = Request()

    @action(methods='post', detail=True, url_name='payments/order/<int:pk>/gateway/')
    def send_user_to_gateway(self, request, pk=None):
        try:
            order = Order.objects.prefetch_related('order_items').get(pk=pk).select_related('order_send')
        except Order.DoesNotExist:
            return Response({"detail": 'order does not exist'}, status.HTTP_400_BAD_REQUEST)


