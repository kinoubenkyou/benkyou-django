from typing import TYPE_CHECKING, Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.forms import ModelForm
from django.urls.base import reverse_lazy
from django.views.generic.edit import UpdateView

from main.models import User

if TYPE_CHECKING:
    UpdateView_ = UpdateView[User, ModelForm[User]]
else:
    UpdateView_ = UpdateView


class UserUpdateView(LoginRequiredMixin, UpdateView_):
    fields = ("username", "first_name", "last_name", "email")
    model = User
    success_url = reverse_lazy("user-read")
    template_name = "form.html"

    def get_object(self, queryset: Optional[QuerySet[User, User]]=None) -> User:
        """Override the object with the authenticated user."""
        user = self.request.user
        assert user.is_authenticated
        return user
