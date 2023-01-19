from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class UserMangerCustom(UserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


# Implement AbstractUser Here
class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=11, null=True, unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    # TODO Implement Manager
    # objects = CustomUserManager()


class Customer(User):
    pass


class Manager(User):
    pass


class Address(models.Model):
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address_detail = models.TextField()
    postal_code = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    receiver_name = models.CharField(max_length=31)
    receiver_phone_number = models.CharField(max_length=16)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)


# Credentials
class Profile(models.Model):
    customer = models.OneToOneField(Customer, related_name='customer_profile', on_delete=models.CASCADE)
