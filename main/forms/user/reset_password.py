from typing import Any

from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.forms import Form
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput
from django.views.decorators.debug import sensitive_variables

from main.models import User


class UserResetPasswordForm(Form):
    password = CharField(widget=PasswordInput(attrs={"autocomplete": "new-password"}))
    password_confirmation = CharField(
        widget=PasswordInput(attrs={"autocomplete": "new-password"})
    )
    token = CharField()
    username = CharField()

    @sensitive_variables("password", "password_confirmation")
    def clean(self) -> None:
        """Validate form-level.

        Validate new password and confirmation match, validate with token in cache.
        """
        password = self.cleaned_data.get("password")
        password_confirmation = self.cleaned_data.get("password_confirmation")
        if password and password_confirmation and password != password_confirmation:
            self.add_error(None, "password and confirmation not match")
        token = self.cleaned_data.get("token")
        username = self.cleaned_data.get("username")
        if token and username:
            sentinel = object()
            cached_token = cache.get(
                f"reset_user_password.{self.cleaned_data['username']}", sentinel
            )
            if cached_token is sentinel:
                self.add_error(None, "token not found")
            elif cached_token != token:
                self.add_error(None, "incorrect token")

    def clean_username(self) -> Any:
        """Validate username found."""
        username = self.cleaned_data["username"]
        if not User.objects.filter(username=username).exists():
            raise ValidationError("username not found")
        return username
