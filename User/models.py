from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator
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
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True)
    phone_number = models.PositiveBigIntegerField(unique=True, null=True, blank=True,
                                                  validators=[RegexValidator
                                                              (r'^989[0-3,9]\d{8}$', 'Enter a valid phone number.',
                                                               'invalid')])

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']


class Customer(User):
    pass


class Manager(User):
    pass


# Credentials
class Profile(models.Model):
    pass


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    receiver_name = models.CharField(max_length=31)
    receiver_phone_number = models.PositiveBigIntegerField()
    province = models.CharField(max_length=31)
    city = models.CharField(max_length=63)
    description = models.TextField()
    postalcode = models.PositiveBigIntegerField()
