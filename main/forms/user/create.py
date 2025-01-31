from django.contrib.auth.forms import BaseUserCreationForm, UserCreationForm

from main.models import User


class UserCreateForm(UserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User  # type: ignore[assignment]
        fields = BaseUserCreationForm.Meta.fields
