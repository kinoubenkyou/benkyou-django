from typing import Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet

from main.models import User
from main.views.read import ReadView


class UserReadView(LoginRequiredMixin, ReadView):
    field_names = (
        "last_login",
        "username",
        "first_name",
        "last_name",
        "email",
        "date_joined",
        "email_is_verified",
    )

    def get_object(self, _queryset: Optional[QuerySet[User, User]] = None) -> User:
        """Override object with authenticated user."""
        user = self.request.user
        return user  # type: ignore[return-value]
