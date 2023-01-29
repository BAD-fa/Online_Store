from django.urls import path
from .views import OrderView, CheckoutView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'order', OrderView, basename='order')
router.register(r'order-checkout', CheckoutView, basename='checkout')
urlpatterns = router.urls
