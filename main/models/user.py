from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=256)
    USERNAME_FIELD = 'email'
