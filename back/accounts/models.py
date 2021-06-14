from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    age = models.CharField(max_length=15)
    height = models.CharField(max_length=15)
    weight = models.CharField(max_length=15)
    sex = models.CharField(max_length=15)
    nickname = models.CharField(max_length=15)
    passwordconfirm = models.TextField(default="")