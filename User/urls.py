from django.urls import path
from .views import *

urlpatterns = [
    # path('', ),
    path('address', UserAddress.as_view(), name='user_addresses'),
    path('information/<int:pk>', CustomerInfo.as_view(), name='customer_info'),
    # path('history'),
]
