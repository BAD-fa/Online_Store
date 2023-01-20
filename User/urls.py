from django.urls import path
from .views import *

urlpatterns = [
    path('', ProfileUrl.as_view(), name='profile_url'),
    path('address', UserAddress.as_view(), name='user_addresses'),
    path('information/<int:pk>', CustomerInfo.as_view(), name='customer_info'),
    # path('history', OrderHistory.as_view(), name='order_history'),
]
