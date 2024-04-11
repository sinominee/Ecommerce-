from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model

# Create your models here.

class User(AbstractUser):
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
