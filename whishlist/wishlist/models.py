from django.db import models


class WishList(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='None')
    product = models.ManyToManyField(Product, through=True, related_name='None', verbose_name='None')

    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now_add=True)
