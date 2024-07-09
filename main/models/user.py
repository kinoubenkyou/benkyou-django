from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.urls import reverse


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=256)
    USERNAME_FIELD = 'email'

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})
