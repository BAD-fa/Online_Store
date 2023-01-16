from django.urls import path
from .views import OrderView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'order', OrderView, basename='order')

urlpatterns = []
urlpatterns += router.urls
