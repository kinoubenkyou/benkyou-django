from typing import TYPE_CHECKING

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from main.forms.user.create import UserCreateForm
from main.models import User
from main.tasks.start_verify_user_email import start_verify_user_email

if TYPE_CHECKING:
    CreateView_ = CreateView[User, UserCreateForm]  # pragma: no cover
else:
    CreateView_ = CreateView


class UserCreateView(CreateView_):
    form_class = UserCreateForm
    success_url = reverse_lazy("user-sign-in")
    template_name = "form.html"

    def form_valid(self, form: UserCreateForm) -> HttpResponse:
        """Queue task to start verify email."""
        response = super().form_valid(form)
        start_verify_user_email.delay(
            self.request.get_host(),
            self.request.scheme,
            self.object.pk,  # type: ignore[union-attr]
        )
        return response
