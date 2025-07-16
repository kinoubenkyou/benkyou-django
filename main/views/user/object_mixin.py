from typing import Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.views import View

from main.models import User


class UserObjectMixin(LoginRequiredMixin, View):
    def get_object(self, _queryset: Optional[QuerySet[User]] = None) -> User:
        """Override object with authenticated user."""
        return self.request.user  # type: ignore[return-value]
