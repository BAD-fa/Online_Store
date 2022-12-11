from django.db import models

from User.models import User


class Category(models.Model):
    title = models.CharField(max_length=63)
    parent_category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="sub_category", null=True)
    is_valid = models.BooleanField(default=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveBigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="products")
    avatar = models.ImageField(upload_to="")  # TODO add upload to path
    description = models.TextField()
    stock = models.PositiveIntegerField()

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)


class Comment(models.Model):
    body = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="comments")  # TODO rename related name
# TODO add Log


class Cart(models.Model):
    pass


class CartItem(models.Model):
    pass


class ProductAttribute(models.Model):
    pass
