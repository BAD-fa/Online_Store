from django.db import models
from django.contrib.auth.models import AbstractUser


# Implement AbstractUser Here
class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=11, null=True, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # TODO Implement Manager
    # objects = CustomUserManager()


class Customer(User):
    pass


class Manager(User):
    pass


# Credentials
class Profile(models.Model):
    pass


class Address(models.Model):
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    geographical_location = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
