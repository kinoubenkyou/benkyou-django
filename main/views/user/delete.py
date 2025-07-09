from typing import TYPE_CHECKING

from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from main.models import User
from main.views.user.user_object_mixin import UserObjectMixin

if TYPE_CHECKING:
    DeleteView_ = DeleteView[User, ModelForm[User]]  # pragma: no cover
else:
    DeleteView_ = DeleteView


class UserDeleteView(UserObjectMixin, DeleteView_):  # type: ignore[misc]
    model = User
    success_url = reverse_lazy("user-sign-in")
    template_name = "form.html"
