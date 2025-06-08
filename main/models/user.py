from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField
from django.db.models.fields import BooleanField


class User(AbstractUser):
    email = EmailField(unique=True)
    email_is_verified = BooleanField()
