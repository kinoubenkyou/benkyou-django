from typing import TYPE_CHECKING, Any

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from main.forms.user.update_password import UserUpdatePasswordForm

if TYPE_CHECKING:
    FormView_ = FormView[UserUpdatePasswordForm]  # pragma: no cover
else:
    FormView_ = FormView


class UserUpdatePasswordView(LoginRequiredMixin, FormView_):
    form_class = UserUpdatePasswordForm
    success_url = reverse_lazy("user-read")
    template_name = "form.html"

    def form_valid(self, form: UserUpdatePasswordForm) -> HttpResponse:
        """Set new password."""
        self.request.user.set_password(form.cleaned_data["new_password"])
        self.request.user.save()
        update_session_auth_hash(self.request, self.request.user)  # type: ignore[arg-type]
        return super().form_valid(form)

    def get_form_kwargs(self) -> dict[str, Any]:
        """Pass user to form."""
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
