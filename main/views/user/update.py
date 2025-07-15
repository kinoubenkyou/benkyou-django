from typing import TYPE_CHECKING

from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from main.models import User
from main.views.user.object_mixin import UserObjectMixin

if TYPE_CHECKING:
    UpdateView_ = UpdateView[User, ModelForm[User]]  # pragma: no cover
else:
    UpdateView_ = UpdateView


class UserUpdateView(UserObjectMixin, UpdateView_):
    fields = ("username", "email")
    model = User
    success_url = reverse_lazy("user-read")
    template_name = "form.html"
