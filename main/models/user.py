from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db.models import EmailField, BooleanField, CharField, ManyToManyField


class User(AbstractBaseUser):
    USERNAME_FIELD = "email"

    objects = BaseUserManager()

    email = EmailField(unique=True)
    email_verified = BooleanField()
    name = CharField(max_length=256)
    organizations = ManyToManyField("Organization", through="Staff")
