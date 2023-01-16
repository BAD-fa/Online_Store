from django.urls import path
from .views import *


urlpatterns = [
    path('categories/', ProductCategoryAPIView.as_view()),
    path('products/', ProductListAPIView.as_view()),
    path('products/detail/', ProductDetailAPIView.as_view()),
]
