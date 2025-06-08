from typing import TYPE_CHECKING, Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from main.forms.user.verify_email import UserVerifyEmailForm

if TYPE_CHECKING:
    FormView_ = FormView[UserVerifyEmailForm]  # pragma: no cover
else:
    FormView_ = FormView


class UserVerifyEmailView(LoginRequiredMixin, FormView_):
    form_class = UserVerifyEmailForm
    success_url = reverse_lazy("user-read")
    template_name = "form.html"

    def form_valid(self, form: UserVerifyEmailForm) -> HttpResponse:
        """Set email as verified, delete token from cache."""
        self.request.user.email_is_verified = True  # type: ignore[union-attr]
        self.request.user.save()
        cache.delete(f"verify_user_email.{self.request.user.id}")
        return super().form_valid(form)

    def get_form_kwargs(self) -> dict[str, Any]:
        """Pass user to form."""
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_initial(self) -> dict[str, Any]:
        """Set initial token value from query string."""
        initial = super().get_initial()
        initial["token"] = self.request.GET.get("token")
        return initial
