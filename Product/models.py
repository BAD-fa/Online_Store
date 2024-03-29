from django.db import models

from Online_Store import settings
from User.models import User


class Category(models.Model):
    title = models.CharField(max_length=63)
    parent_category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="sub_category",
                                        null=True, blank=True)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveBigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="products")
    avatar = models.ImageField(upload_to="", blank=True, null=True)  # TODO add upload to path
    description = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField()

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                             related_name="comments")  # TODO rename related name

    is_valid = models.BooleanField(default=False)

    def clean(self):
        user_purchased = None  # TODO get user's purchased products in this field
        if self.product in user_purchased:
            self.is_valid = True
        else:
            self.is_valid = False


# Cart and Cart Item fields must be similar to Order and Order item
class Cart(models.Model):
    pass


class CartItem(models.Model):
    pass
