from typing import TYPE_CHECKING

from django.contrib.auth.forms import (
    UserCreationForm,
    UsernameField,
)

from main.models import User

if TYPE_CHECKING:
    UserCreationForm_ = UserCreationForm[User]  # pragma: no cover
else:
    UserCreationForm_ = UserCreationForm


class UserCreateForm(UserCreationForm_):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        field_classes = {"username": UsernameField}

    def save(self, commit: bool = True) -> User:
        """Set email_is_verified to False."""
        self.instance.email_is_verified = False
        return super().save(commit=commit)
