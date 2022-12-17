from django.db import models
from django.utils import timezone

from Online_Store import settings
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
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                             related_name="comments")  # TODO rename related name


# Cart and Cart Item fields must be similar to Order and Order item
class Cart(models.Model):
    class CartStatus(models.TextChoices):
        OPEN = "OPEN"
        CLOSED = "CLOSED"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    product = models.ManyToManyField(Product, related_name='cart')
    status = models.CharField(max_length=6, choices=CartStatus.choices, default=CartStatus.CLOSED)
    total_price = models.PositiveBigIntegerField(default=0)
    discount = models.PositiveBigIntegerField(default=0)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_item")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    expire_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(hours=1))
    count = models.PositiveSmallIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
