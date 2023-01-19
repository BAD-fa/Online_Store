from django.urls import path
from .views import *

urlpatterns = [
    # path('', ),
    path('address', UserAddress.as_view(), name='user_addresses'),
    # path('information'),
    # path('history'),
]
