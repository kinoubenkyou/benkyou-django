from typing import Any

from django.contrib.auth.forms import UsernameField
from django.core.exceptions import ValidationError
from django.forms.forms import Form
from django.forms.widgets import TextInput

from main.models import User


class UserStartResetPasswordForm(Form):
    username = UsernameField(widget=TextInput(attrs={"autofocus": True}))

    def clean_username(self) -> Any:
        """Validate username found."""
        return_ = self.cleaned_data["username"]
        if not User.objects.filter(username=return_).exists():
            raise ValidationError("username not found")
        return return_
