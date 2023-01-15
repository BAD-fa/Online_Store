from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import *


# Category Related APIView----------------------------------------------------------------------------------------------
class ProductCategoryAPIView(GenericAPIView):

    @staticmethod
    def get(request):
        all_categories = Category.objects.all()

        result = {}
        for category in all_categories:
            if not category.parent_category:
                result[f'{category.pk}'] = category.title

        return Response(result)

    @staticmethod
    def post(request):
        user_choice = request.data['category']
        all_categories = Category.objects.all()
        target_categories = all_categories.filter(title__contains=user_choice)

        result = {}
        for category in target_categories:
            sub_categories = all_categories.filter(parent_category=category)

            category_info = {}
            for sub_cat in sub_categories:
                category_info[f'{sub_cat.pk}'] = sub_cat.title

            result[f'{category.title}'] = category_info

        return Response(result)
