from django.urls import path

from Product.views import CartList, CartDetail, CartItemList

urlpatterns = [
    path('cart/', CartList.as_view()),
    path('cart/<int:pk>', CartDetail.as_view()),
    path('cart-item/', CartItemList.as_view()),
    path('cart-item/<int:pk>', CartDetail.as_view()),
]
