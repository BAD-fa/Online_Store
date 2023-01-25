from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView

from seializers import WishListSerializer
from permissions import IsOwner
from models import WishList


class WishListAPI(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = WishListSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        return WishList.objects.fitler(user=user)
