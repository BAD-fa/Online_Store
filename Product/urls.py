from django.urls import path
from .views import *


urlpatterns = [
    path('categories/', CategoryAPIView.as_view()),
    path('categories/subcategories/', SubCategoryAPIView.as_view()),
    path('products/', ProductListAPIView.as_view()),
    path('products/detail/', ProductDetailAPIView.as_view()),

    path('search/', SearchAPIview.as_view()),

    path('home/', HomePage.as_view()),
]
