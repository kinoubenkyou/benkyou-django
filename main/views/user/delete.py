from typing import TYPE_CHECKING, Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.forms import ModelForm
from django.urls.base import reverse_lazy
from django.views.generic.edit import DeleteView

from main.models import User

if TYPE_CHECKING:
    DeleteView_ = DeleteView[User, ModelForm[User]]
else:
    DeleteView_ = DeleteView


class UserDeleteView(LoginRequiredMixin, DeleteView_):  # type: ignore[misc]
    model = User
    success_url = reverse_lazy("user-sign-in")
    template_name = "form.html"

    def get_object(self, queryset: Optional[QuerySet[User, User]] = None) -> User:
        """Override the object with the authenticated user."""
        user = self.request.user
        assert user.is_authenticated
        return user
