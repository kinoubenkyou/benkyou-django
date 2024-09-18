from django.forms import ModelForm

from main.models import User


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ("name",)
