from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField
from django.db.models.fields import BooleanField
from django.utils.translation import gettext_lazy


class User(AbstractUser):
    email = EmailField(gettext_lazy("email address"), unique=True)
    email_is_verified = BooleanField()
