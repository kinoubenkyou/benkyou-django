from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models import Manager
from django.urls import reverse


class UserManager(Manager):
    """
    Based on django.contrib.auth.base_user.BaseUserManager
    """

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})

    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the email address by lowercasing the domain part of it.
        """
        email = email or ""
        try:
            email_name, domain_part = email.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            email = email_name + "@" + domain_part.lower()
        return email


class User(AbstractBaseUser):
    """
    Based on django.contrib.auth.models.AbstractUser
    """

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=256)

    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_absolute_url(self):
        return reverse("user-detail", kwargs={"pk": self.pk})
