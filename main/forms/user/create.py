from typing import TYPE_CHECKING

from django.contrib.auth.forms import BaseUserCreationForm, UserCreationForm

from main.models import User

if TYPE_CHECKING:
    UserCreationForm_ = UserCreationForm[User]
else:
    UserCreationForm_ = UserCreationForm


class UserCreateForm(UserCreationForm_):
    class Meta(BaseUserCreationForm.Meta):  # type: ignore[name-defined, misc]
        model = User
