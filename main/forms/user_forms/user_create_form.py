from django.contrib.auth.forms import BaseUserCreationForm

from main.models import User


class UserCreateForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ("email", "name")

    def save(self, commit=True):
        self.instance.email_verified = False
        return super().save(commit)
