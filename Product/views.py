from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist

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
                # TODO Add 'Product list' Related API

            result[f'{category}'] = category_info

        return Response(result)


# Product Related APIView-----------------------------------------------------------------------------------------------
class ProductListAPIView(GenericAPIView):

    @staticmethod
    def get(request):
        try:
            target_category = request.data['category']
            category = Category.objects.get(title=target_category)
        except KeyError:
            return Response('category title field is required.')
        except ObjectDoesNotExist:
            return Response('category title does not exist.')

        products = category.products.all()

        result = {}
        product_info = {}
        for product in products:

            avatar = product.avatar
            if not avatar:
                avatar = 'No Image'

            product_info[f'{product.name}'] = {
                'avatar': avatar,
                'price': product.price,
                'rate': 'None'
            }
            # TODO Add 'product detail link'
            # TODO Update 'Product rate'

        result[f'{category}'] = product_info

        return Response(result)


class ProductDetailAPIView(GenericAPIView):

    @staticmethod
    def get(request):
        try:
            target_product = request.data['product']
            product = Product.objects.get(name=target_product)
        except KeyError:
            return Response('product title field is required.')
        except ObjectDoesNotExist:
            return Response('product title does not exist.')

        result = {}

        avatar = product.avatar
        if not avatar:
            avatar = 'No Image'

        comments = {}
        for comment in product.comments.all():
            comments[f'{comment.user.username}'] = {'comment': comment.body, 'date': comment.date}

        result[f'{product.name}'] = {
            'description': product.description,
            'avatar': avatar,
            'price': product.price,
            'stock': product.stock,
            'rate': 'Add',
            'comments': comments,
        }
        # TODO Add 'Comment' Related API
        # TODO Add 'rate' Related API
        # TODO Add 'Add/Remove to cart' Related API
        # TODO Add 'Add/Remove to wishlist' Related API

        return Response(result)

# HomePage APIView------------------------------------------------------------------------------------------------------
class HomePage(GenericAPIView):
    # TODO Add 'Profile' Related API
    # TODO Add 'LOGIN/Register - Logout' Related API
    # TODO Add 'Category List' Related API
    # TODO Add 'Top Rated Products(10)'
    # TODO Add 'Search' Related API
    pass
