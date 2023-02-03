from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('ratings/<int:id>/', views.RatingViewSet.as_view(
            {'get': 'list', 'post': 'create'})),
]