from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist

from .serializers import *

BASE_DIR = 'http://127.0.0.1:8000/'

# Search Related APIView------------------------------------------------------------------------------------------------

class SearchAPIview(GenericAPIView):
    @staticmethod
    def get(request):
        try:
            search = request.data['search']
        except KeyError:
            return Response('search field is required.')

        products = Product.objects.filter(name__contains=search)

        result = {}

        for product in products:
            avatar = product.avatar
            if not avatar:
                avatar = 'No Image'

            result[f'{product}'] = {
                'avatar': avatar,
                'price': product.price,
                'rate': 'update rate'
            }
            # TODO Update 'Product rate'

        result['products'] = BASE_DIR + 'products/detail/'
        return Response(result)


# Category Related APIView----------------------------------------------------------------------------------------------
class CategoryAPIView(GenericAPIView):

    @staticmethod
    def get(request):
        all_categories = Category.objects.all()

        result = {}
        for category in all_categories:
            if not category.parent_category:
                result[f'{category.pk}'] = category.title

        result['subcategories'] = BASE_DIR + 'categories/subcategories/'
        return Response(result)


class SubCategoryAPIView(GenericAPIView):
    @staticmethod
    def get(request):
        try:
            user_choice = request.data['category']
        except KeyError:
            return Response('category field is required.')

        all_categories = Category.objects.all()
        target_categories = all_categories.filter(title__contains=user_choice)

        result = {}
        for category in target_categories:
            if not category.parent_category:
                sub_categories = all_categories.filter(parent_category=category)

                category_info = {}
                for sub_cat in sub_categories:
                    category_info[f'{sub_cat.pk}'] = sub_cat.title

                result[f'{category}'] = category_info

        result['products'] = BASE_DIR + 'products/'
        return Response(result)


# Product Related APIView-----------------------------------------------------------------------------------------------
class ProductListAPIView(GenericAPIView):

    @staticmethod
    def get(request):
        try:
            target_category = request.data['category']
            category = Category.objects.get(title=target_category)
        except KeyError:
            return Response('category field is required.')
        except ObjectDoesNotExist:
            return Response('category does not exist.')

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
                'rate': 'update rate'
            }
            # TODO Update 'Product rate'

        result[f'{category}'] = product_info

        result['products'] = BASE_DIR + 'products/detail/'
        return Response(result)


class ProductDetailAPIView(GenericAPIView):

    @staticmethod
    def get(request):
        try:
            target_product = request.data['product']
            product = Product.objects.get(name=target_product)
        except KeyError:
            return Response('product field is required.')
        except ObjectDoesNotExist:
            return Response('product does not exist.')

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
        # TODO Add 'Add/Remove to cart' Related API
        # TODO Add 'Add/Remove to wishlist' Related API

        # TODO Check if user buy this product or not
        result['rate'] = BASE_DIR + f'ratings/{product.id}/'

        return Response(result)

# HomePage APIView------------------------------------------------------------------------------------------------------
class HomePage(GenericAPIView):
    @staticmethod
    def get(request):
        result = {
            'profile': BASE_DIR + 'profile/',
            'search': BASE_DIR + 'search/',
            'categories': BASE_DIR + 'categories/'
        }
        # TODO Add 'LOGIN/Register - Logout' Related API
        # TODO Add 'Top Rated Products(10)'
        return Response(result)
