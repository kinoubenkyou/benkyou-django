from typing import TYPE_CHECKING

from django.forms import ModelForm
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView

from main.forms.user import UserCreateForm
from main.models import User

if TYPE_CHECKING:
    CreateView_ = CreateView[User, ModelForm[User]]
else:
    CreateView_ = CreateView


class UserCreateView(CreateView_):
    form_class = UserCreateForm
    success_url = reverse_lazy("user-sign-in")
    template_name = "form.html"
