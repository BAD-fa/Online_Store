from django.db import models

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
    is_valid = models.BooleanField(default=True)


class AbstractComment(models.Model):
    CREATED = 10
    APPROVED = 20
    REJECTED = 30
    DELETED = 40

    COMMENT_CHOICE = (
        (CREATED, 'Created'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        (DELETED, 'Deleted')
    )

    parent_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='none')
    # TODO related_name
    body = models.TextField()
    status = models.PositiveSmallIntegerField(choices=COMMENT_CHOICE, default=CREATED, blank=False)
    validated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # TODO related_name
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = False  # TODO turn True while production


class CartItem(models.Model):
    pass
