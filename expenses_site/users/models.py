from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

# Create your models here.

class User(AbstractUser):
    is_verified_email = models.BooleanField(default=False)