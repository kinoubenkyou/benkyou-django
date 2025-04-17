from typing import TYPE_CHECKING, Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import HttpResponse
from django.views.generic import FormView
from rest_framework.reverse import reverse_lazy

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
        """Set the email as verified, delete the token from the cache."""
        self.request.user.email_is_verified = True  # type: ignore[union-attr]
        self.request.user.save()
        cache.delete(f"verify_user_email.{self.request.user.id}")
        return super().form_valid(form)

    def get_form_kwargs(self) -> dict[str, Any]:
        """Pass the user id to the form."""
        kwargs = super().get_form_kwargs()
        kwargs["user_id"] = self.request.user.id
        return kwargs

    def get_initial(self) -> dict[str, Any]:
        """Set initial token value from the query string."""
        initial = super().get_initial()
        initial["token"] = self.request.GET.get("token")
        return initial
