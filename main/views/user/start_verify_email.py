from typing import TYPE_CHECKING

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import Form
from django.http import HttpResponse
from django.views.generic import FormView
from rest_framework.reverse import reverse_lazy

from main.tasks import start_verify_user_email

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
        response = super().form_valid(form)
        start_verify_user_email.delay(
            self.request.get_host(),
            self.request.scheme,
            self.request.user.pk,
        )
        return response
