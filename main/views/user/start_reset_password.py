from typing import TYPE_CHECKING

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from main.forms.user.start_reset_password import UserStartResetPasswordForm
from main.tasks.start_reset_user_password import start_reset_user_password

if TYPE_CHECKING:
    FormView_ = FormView[UserStartResetPasswordForm]  # pragma: no cover
else:
    FormView_ = FormView


class UserStartResetPasswordView(FormView_):
    form_class = UserStartResetPasswordForm
    success_url = reverse_lazy("user-sign-in")
    template_name = "form.html"

    def form_valid(self, form: UserStartResetPasswordForm) -> HttpResponse:
        """Queue task to start reset password."""
        start_reset_user_password.delay(
            self.request.get_host(),
            self.request.scheme,
            form.cleaned_data["username"],
        )
        return super().form_valid(form)
