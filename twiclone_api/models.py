from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    phone = PhoneNumberField(null=True, blank=True)
    bio = models.CharField(max_length=160, null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    class Meta:
        ordering = ['-create_date']
