from django.contrib.auth.forms import BaseUserCreationForm

from main.models import User


class UserCreateForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name')
