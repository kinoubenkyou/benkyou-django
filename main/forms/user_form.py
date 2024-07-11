from django.contrib.auth.forms import BaseUserCreationForm, UserChangeForm
from django.forms import ModelForm

from main.models import User


class UserCreateForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name')


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('name',)
