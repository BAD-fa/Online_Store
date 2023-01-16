from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order
from .serializers import OrderAllDetailSerializer, OrderViewSerializer, OrderSendSerializer
from .utils import orders, order_items


class OrderView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderViewSerializer
    queryset = Order.objects.prefetch_related('order_items').all()

    def get_object(self):
        obj = super(OrderView, self).get_object()
        orders.check_order(obj)
        return obj

    # def retrieve(self, request, pk, *args, **kwargs):
    #     order = get_object_or_404(Order, pk)
    #     order.save()
    #     serializer = OrderViewSerializer(instance=order)
    #     return Response(serializer.data)

    def get_queryset(self):
        if self.action == 'list':
            return Order.objects.filter(user=self.request.user)
        else:
            return super(OrderView, self).get_queryset()


class CheckoutView(ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = OrderSendSerializer(request)
        serializer.save()


