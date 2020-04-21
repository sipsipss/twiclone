from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from phonenumber_field.modelfields import PhoneNumberField
import os


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.username, instance.create_date, ext)
    return os.path.join('profile_picture', filename)


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    create_date = models.DateField(auto_now_add=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ['-create_date']


class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    avatar = ProcessedImageField(null=True, blank=True,
                                 upload_to=content_file_name,
                                 processors=[ResizeToFill(400, 400)],
                                 format='JPEG',
                                 options={'quality': 75}
                                 )
    username = models.OneToOneField(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE)
    phone = PhoneNumberField(null=True, blank=True)
    bio = models.CharField(max_length=160, null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date']


class UserTweet(models.Model):
    tweet = models.CharField(max_length=280)
    retweet = models.PositiveIntegerField()
    like = models.PositiveIntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
