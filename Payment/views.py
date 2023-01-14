from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ViewSet
from .models import Order
from rest_framework.permissions import IsAuthenticated


class CheckoutView(ViewSet):
    permission_classes = [IsAuthenticated]

    def retrive(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        return None