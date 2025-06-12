from typing import Any

from django.core.exceptions import ValidationError
from django.forms import CharField, PasswordInput
from django.views.decorators.debug import sensitive_variables

from main.forms.user import UserForm


class UserUpdatePasswordForm(UserForm):
    old_password = CharField()
    new_password = CharField(
        widget=PasswordInput(attrs={"autocomplete": "new-password"})
    )
    new_password_confirmation = CharField(
        widget=PasswordInput(attrs={"autocomplete": "new-password"})
    )

    @sensitive_variables("old_password")
    def clean_old_password(self) -> Any:
        """Validate with user password."""
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError("incorrect old password")
        return old_password

    @sensitive_variables("new_password", "new_password_confirmation")
    def clean(self) -> None:
        """Validate new password and confirmation match."""
        new_password = self.cleaned_data.get("new_password")
        new_password_confirmation = self.cleaned_data.get("new_password_confirmation")
        if (
            new_password
            and new_password_confirmation
            and new_password != new_password_confirmation
        ):
            self.add_error(None, "new password and confirmation not match")
