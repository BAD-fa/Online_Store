from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [

]

urlpatterns += router.urls