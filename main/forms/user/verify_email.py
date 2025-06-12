from typing import Any

from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.forms import CharField

from main.forms.user import UserForm


class UserVerifyEmailForm(UserForm):
    token = CharField()

    def clean_token(self) -> Any:
        """Validate with token in the cache."""
        token = self.cleaned_data["token"]
        sentinel = object()
        cached_token = cache.get(f"verify_user_email.{self.user.id}", sentinel)
        if cached_token is sentinel:
            raise ValidationError("token not found")
        elif cached_token != token:
            raise ValidationError("incorrect token")
        return token
