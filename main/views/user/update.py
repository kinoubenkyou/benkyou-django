from typing import TYPE_CHECKING, Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from main.models import User

if TYPE_CHECKING:
    UpdateView_ = UpdateView[User, ModelForm[User]]  # pragma: no cover
else:
    UpdateView_ = UpdateView


class UserUpdateView(LoginRequiredMixin, UpdateView_):
    fields = ("username", "email")
    model = User
    success_url = reverse_lazy("user-read")
    template_name = "form.html"

    def get_object(self, _queryset: Optional[QuerySet[User, User]] = None) -> User:
        """Override object with authenticated user."""
        user = self.request.user
        return user  # type: ignore[return-value]
