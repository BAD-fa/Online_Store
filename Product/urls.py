from django.urls import path
from .views import *


urlpatterns = [
    path('categories/', ProductCategoryAPIView.as_view()),
]
