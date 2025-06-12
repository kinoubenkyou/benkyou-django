from typing import TYPE_CHECKING

from django.forms import CharField, ModelForm, PasswordInput
from django.views.decorators.debug import sensitive_variables

from main.models import User

if TYPE_CHECKING:
    ModelForm_ = ModelForm[User]  # pragma: no cover
else:
    ModelForm_ = ModelForm


class UserCreateForm(ModelForm_):
    password = CharField(widget=PasswordInput(attrs={"autocomplete": "new-password"}))
    password_confirmation = CharField(
        widget=PasswordInput(attrs={"autocomplete": "new-password"})
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    @sensitive_variables("password", "password_confirmation")
    def clean(self) -> None:
        """Validate password and confirmation match."""
        password = self.cleaned_data.get("password")
        password_confirmation = self.cleaned_data.get("password_confirmation")
        if password and password_confirmation and password != password_confirmation:
            self.add_error(None, "password and confirmation not match")

    def save(self, commit: bool = True) -> User:
        """Set email as not verified, set password."""
        self.instance.email_is_verified = False
        self.instance.set_password(self.cleaned_data["password"])
        return super().save(commit=commit)
