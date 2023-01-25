from django.urls import path
from views import WishListAPI

urlpatterns += [path('wishlist', WishListAPI.as_view(), name='Wish List'), ]
