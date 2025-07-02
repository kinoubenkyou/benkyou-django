from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db.models import BooleanField, CharField, EmailField


class User(AbstractBaseUser):
    USERNAME_FIELD = "username"
    email = EmailField(unique=True)
    email_is_verified = BooleanField()
    objects = BaseUserManager()
    password = CharField()
    username = CharField(unique=True)
