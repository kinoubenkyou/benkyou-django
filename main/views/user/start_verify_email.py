from typing import TYPE_CHECKING

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.forms import Form
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from main.tasks.start_verify_user_email import start_verify_user_email

if TYPE_CHECKING:
    FormView_ = FormView[Form]  # pragma: no cover
else:
    FormView_ = FormView


class UserStartVerifyEmailView(LoginRequiredMixin, FormView_):
    form_class = Form
    success_url = reverse_lazy("user-read")
    template_name = "form.html"

    def form_valid(self, form: Form) -> HttpResponse:
        """Queue task to start verify email."""
        start_verify_user_email.delay(
            self.request.get_host(),
            self.request.scheme,
            self.request.user.pk,
        )
        return super().form_valid(form)
